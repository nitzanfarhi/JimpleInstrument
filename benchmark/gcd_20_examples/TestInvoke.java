class TestInvoke {
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
  
}
