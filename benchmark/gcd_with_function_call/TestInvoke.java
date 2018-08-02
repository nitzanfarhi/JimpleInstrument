class TestInvoke {
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
  
}
