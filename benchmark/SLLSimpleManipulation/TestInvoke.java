class TestInvoke {
  private static int calls=0;
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
