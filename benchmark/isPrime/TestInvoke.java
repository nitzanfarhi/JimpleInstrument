class TestInvoke {
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
  
}
