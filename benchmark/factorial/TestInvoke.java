class TestInvoke {
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
  
}
