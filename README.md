---
abstract: |
    This paper is submitted as a final report and a documentation of the
    final product. The final product is a software that is able to generate
    spec files out of a running java code. spec files are traces that are
    used as input for synthesis algorithms. First, we will explain about our
    first attempt implementing this by using instrumentation which is not
    perfect. After that, we will explain about the second attempt of
    implementation, using Soot library.
author:
- |
    Students: Nitzan Farhi, nitzanfa@post.bgu.ac.il\
    and Matan Kintzlinger, matankin@post.bgu.ac.il
title: |
    Program Analysis and Verification\
    Project
---

Theory
======

On both implementations, the final target is to modify byte-code while
it is running, the modification will be like so: after each command that
is run by the JVM, a command that was created by our library will be
injected. This command will print description of the previous command
into a spec file, this description will include the command itself and
the state of the program after this command.

Implementation using Instrumentation
====================================

The code is provided at: <https://github.com/nitzan2611/Jagent>.\
Java Byte-code Instrumentation is a way for adding byte-code to a java
class during it’s run-time. This is done by creating a jar that contains
a java class with the function:

    public static void premain(String args, Instrumentation instrumentation)

Wheres **args** is a String that the user could provide arguments in,
and instrumentation is used for the instrumentation. Later, when
instrumenting a class by calling:

    java -javaagent:agent.jar=argumentstring -cp tested.jar Foo.Main

whereas **agent.jar** is the created jar, **argumentstring** is the
string provided to the **premain** and **tested.jar** is the software
that is instrumented. We used the ByteBuddy[^1] library in order to make
the instrumentation easier. We used an annotation in order to mark the
function we want to instrument, when this function is called, the agent
code will run before the function’s code, also the agent code will run
after the function’s code. We parsed the parameters of the function when
it is called and the return value of the function when it finishes. (We
couldn’t manage to append a command of our own after each command inside
the function but only before and after the whole function, this is why
we moved to Soot instead).

Implementation using Soot Library
=================================

The code is provided at:
<https://github.com/nitzan2611/JimpleInstrument>.\

Background
----------

Soot[^2] is a java optimization framework, which provides an
intermediate representation of java, called Jimple , to make
optimizations or modifications on. This can also be used as a way of
modifying java program in order to make it generate spec files.

Running the instrumenter
------------------------

To run the instrumenter the command:

    java MainDriver classname [options]

need to be run where **classname** is the name of the class that is
wanted to be instrumented and options are flags that can be added :

1.  -d for the delta option

After running this command, **classname** was instrumented. That we can
run it as we would regularly would. We can notice that a spec file was
also generated.

Implementation
--------------

### mainDriver class

In the mainDriver java class, after parsing the arguments, we called the
commands:

           Pack jtp = PackManager.v().getPack("jtp");
           jtp.add(new Transform("jtp.instrumenter",
                                 new InvokeStaticInstrumenter()));

This will call a new class that we created, called
**InvokeStaticInstrumenter**, which is in charge of the instrumentation.
After that, soot is ran with the appropriate classes. (Of course soot’s
classpath was appended with the folder that the files are in).

### InvokeStaticInstrumeneter

Every method instrumentation starts at

    protected void internalTransform(Body body, String phase, Map options)

We add commands to 2 different methods:

-   The main method - which we add commands before it’s return
    statements in the method **instrumentReturn**

-   An annotated method with the @checker annotation - this is the one
    the library will generate a spec file of.

When instrumenting a method, 3 kinds of commands are added to the jimple
code that soot supply us with: when entering the method, which is
handled by **instrumentBegin**, after every command in the function’s
buddy, which is handled by **instrumentAnyCommand**, and when exiting
the method, which is handled by **instrumentMethodFinish**.\
When instrumenting commands in the function, a linked list of jimple
commands is provided by soot, we iterated this link list and used the
pattern matcher in the Util library [^3] in order to match the Jimple
statement into a correct object using the MyMatcher class, after that
the command is printed in the spec file. After printing the command, the
state of the JVM is printed.\
Printing the state of an object is done via a call to the function
**PrintLocalValue**.

#### PrintLocalValue

This method iterates over all ints and objects in the JVM and
diffrentitate between them. Then, it copies the value of the int or the
address of the object into a value in the MyCounter class. After that a
method that is responsible of printing those values and their name is
called.

### MyCounter

This is a helper class that contains all the functions that are
instrumented to be called. This class also contains variables for the
same purpose. Some of the more meaning-full ones are:

-   **init** which is called when an annotated method is called and it’s
    purpose is to create the spec file and some of it’s prefix.

-   **printValue, printParamValue, printObjValue and
    printParamObjValue** are used to print the state of objects and ints
    if they are parameters or not.

-   **methodFinish** is called when an annotated method is finished in
    order to add the sufix of an example in the spec file

-   **finish** is called when the whole program exists in order to close
    the spec file.

### MyMatcher

This class is in charge of matching strings into jimple objects such as
**CaseAssignLocal\_InstanceFieldRef, CaseAssignLocal\_Invoke,
CaseAssignInstanceFieldRef, etc** in the end it returns the command in a
format that is recognized and can be parsed by pexyn interpeter.

Benchmarks
==========

In this section we will describe our experiments and evaluation using
benchmarks we created (which is located in the Github repository also),
we will elaborate each experiment in the benchmarks. Each experiment is
located in a folder inside the benchmarks folder. Each folder contains 4
items:

1.  TestInvoke.java - the java file under test

2.  dot.class - folder that contains .class and .jimple outputs of our
    software

3.  output.spec - the spec formatted output file of our software

4.  visual-output - folder that contains the output of pexyn of
    output.spec

factorial
---------

This experiment computes the factorial of the numbers 1,2,..,6

      public static void main(String[] args) {
          for(int i=1;i<6;i++)
              factorial(i);
      }
      
      @checker
      private static int factorial(int num) {
          int i,fact=1;  
          for(i=1;i<=num;i++){    
              fact=fact*i;    
          }    
          return fact;
      }

gcd
---

This experiment computes the GCD of 120 and 16

      public static void main(String[] args) {
          gcd(120,16);
      }
      @checker
      private static int gcd(int a, int b) {
          while (a != b) {
                if (a > b) {
                  a = a - b;
                }
                else {
                  b = b - a;              
                }
              }
          return a;
      }

20 GCD computations
-------------------

This experiment computes 20 GCD computations for the numbers
\[125,34\],\[126,35\],...\[144,53\]

        public static void main(String[] args) {
          for(int i=125,j=34,m=0;m<20;m++,i++,j++)
              gcd(i,j);
      }
      @checker
      private static int gcd(int a, int b) {
          while (a != b) {
                if (a > b) {
                  a = a - b;
                }
                else {
                  b = b - a;              
                }
              }
          return a;
      }

GCD with function calls
-----------------------

This experiment calculate the same GCDs as in the last experiment but
this time the GCD algorithm uses 2 external functions in order to
calculate substraction

        public static void main(String[] args) {
          for(int i=125,j=34,m=0;m<20;m++,i++,j++)
              gcd(i,j);
      }
      

      private static int getA(int a, int b) {
          return a - b;
      }

      private static int getB(int a, int b) {
          return b - a;
      }
      @checker
      private static int gcd(int a, int b) {
          while (a != b) {
                if (a > b) {
                  a = getA(a,b);
                }
                else {
                  b = getB(a,b);              
                }
              }
          return a;
      }

isPrime
-------

This experiment checks if the numbers \[30,31..,39\] are prime

         public static void main(String[] args) {
          for(int i=30;i<40;i++)
              isPrime(i);
      }
      
      
      @checker
      private static int isPrime(int num) {
          for(int i=2;i<num;i++) {
            for(int j=1;j<num;j++)
                if(i*j==num)
                    return 0;
        }
        return num;
      }

SLL\_Simple\_Manipulation
-------------------------

This experiment creates an SLL node and changes it’s default value from
0 to 3.

        public static void main(String[] args) {
          SLLSimpleManipulation(new SLL());
      }
      @checker
      private static int SLLSimpleManipulation(SLL sll) {
          sll.d=3;
          return 6;
      }

    }
    class SLL{
        int d=0;
        SLL l=null;
        SLL r=null;
        SLL(int x){
            d = x;
        }
        SLL(){}
    }

SLL\_Manipulation
-----------------

This experiment creates an SLL (**S**ingle **L**inked **L**ist) with the
values 2,3,4,5. After that the values are changed to 13,12,11,10 and the
nodes are connected one after another. Later, the algorithm iterates
over the SLL and if the node’s value is bigger than 3, the data is
subtracted by 1, else if it is bigger, 2 is subtracted, else 3 is
subtracted.

      class TestInvoke {
      public static void main(String[] args) {
        for (int i=1; i<12; i+=1) {
          System.out.println(SLLManipulation(new SLL(),new SLL(2),new SLL(3),new SLL(4),new SLL(5),3));
        } 
      }
      @checker
      private static int SLLManipulation(SLL sll,SLL n1, SLL n2, SLL n3, SLL n4, int x){
          int c =33;
          n1.d=13;
          n2.d=12;
          n3.d=11;
          n4.d=10;
          n1.l=n2;
          n2.l=n3;
          n3.l=n4;
          SLL tmp=n1;
          while(tmp!=null)
          {
              c++;
              if(tmp.d>x) {
                  tmp=tmp.l;
                  x=x-1;
              }
              else if(tmp.d<x) {
                  tmp=tmp.r;
                  x=x-2;
              }
              else if(tmp.d==x) {
                  x=x-3;
                  return tmp.d;
              }
          }
          return c;
      }

    }
    class SLL{
        int d=0;
        SLL l=null;
        SLL r=null;
        SLL(int x){
            d = x;
        }
        SLL(){}
    }

Reflection
==========

In the beginnig the project was very difficult for us since
instrumenting bytecode using java agent is very low level, after that by
using soot life was a bit easier but still required many compilation
error and bugs since the soot library is not perfect, in the end we
understood the importance of the project and learned a lot about
instrumentation and it’s significance.\
\

[^1]: <http://bytebuddy.net/>

[^2]: <https://github.com/Sable/soot>

[^3]: <https://github.com/rumster/Util>
