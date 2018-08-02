class TestInvoke {
  private static int calls=0;
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
}

