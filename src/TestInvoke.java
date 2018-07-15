class TestInvoke {
  private static int calls=0;
  public static void main(String[] args) {
 
    for (int i=1; i<12; i+=1) {
      System.out.println(goo(new SLL(),new SLL(2),new SLL(3),new SLL(4),new SLL(5),3));
//      System.out.println(goo2(i,3));
    } 
//    goo(12,3);
  }

  private static int foo(int a) {
	  return a;
  }
//  @checker
  private static int goo2(int a, int b) {
	  int c =32;
	  while (a != b) {
		  a = foo(a);
		    if (a > b) {
		      a = a - b;
		    }
		    else {
		    	c=c-a;
		      b = b - a;		      
		    }
		  }
	  return c;
  }
  volatile static int a;
  @checker
  private static int goo(SLL sll,SLL n1, SLL n2, SLL n3, SLL n4, int x){
	  int c =33;
//	  while (a != b) {
//		  a = foo(a);
//		    if (a > b) {
//		      a = a - b;
//		    }
//		    else {
//		    	c=c-a;
//		      b = b - a;		      
//		    }
//		  }
//	  return c;
//	  SLL n1 = new SLL();
//	  SLL n2 = new SLL();
//	  SLL n3 = new SLL();
	  a = 13;
	  n1.d=a;
	  a=12;
	  n2.d=a;
	  a=11;
	  n3.d=a;
	  a=10;
	  n4.d=a;

	  n1.l=n2;
	  n2.l=n3;
	  n3.l=n4;
//	  n5.l=n4;
	  
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

	  //return 1;
//  }
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
/*
class TestInvoke {
private static int calls=0;
public static void main(String[] args) {

  SLL head = new SLL();
  head.d=50;
  SLL tmp = head;
for(int i=0;i<10;i++)
{
	SLL t = new SLL();
	t.d=i;
	tmp.n=t;
	tmp=tmp.n;
}
while(head.n!=null)
{
	System.out.println(head.d);
	head=head.n;
}
}

@checker
private static void fill(SLL head,int val){
  SLL t;
  t = head;
  while (t != null) {
    t.d = val;
    t = t.n;
  }
}

}

*/