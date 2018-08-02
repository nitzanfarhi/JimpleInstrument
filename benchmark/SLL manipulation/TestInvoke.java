class TestInvoke {
  private static int calls=0;
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
