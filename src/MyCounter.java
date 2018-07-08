import java.io.BufferedWriter;
import java.io.File;
import java.io.FileOutputStream;
import java.io.FileWriter;
import java.io.IOException;
import java.io.OutputStreamWriter;
import java.io.PrintWriter;
import java.util.ArrayList;
import java.util.HashMap;

public class MyCounter {
  private static PrintWriter writer=null;
  public static String name="x";
  public static int value=5;
  public static Object objvalue=null;
  public static int SHOW_DELTA=0; 
  public static int DELTA_CHANGED=0; 
  public static HashMap<String,String> map;
  public static void addVar(String name,String value)
  {
	  map.put(name,value);
  }
  public static void toggleDelta()
  {
	  if(DELTA_CHANGED==0) {
		  SHOW_DELTA=(SHOW_DELTA==1)?0:1;
		  DELTA_CHANGED=1;
	  }
  }
  public static void init(String out)
  {
	  try {
		  if(writer==null)
		  {
			  curr=new ArrayList();
			  writer= new PrintWriter(new FileWriter("output.spec"));
			  writer.println(out);
			  writer.flush();
		  }
		  writer.print("\texample {[");
	} catch (IOException e) {
		System.out.println(e.getMessage());
	}
	  name="ERROR";
	  value=-1;
	  curr = new ArrayList();
	  
  }
  public static void method_finish()
  {
	  if(writer!=null)
	  {
		  writer.println("\n\t}");
		  writer.flush();
	  }
	  else System.out.println("Error");
  }
  static ArrayList<String> last=null;
  static ArrayList<String> curr=null;
  public static void printObjValue(int end)
  {
	  if(objvalue==null) objvalue=1;
	  String s;
	  if(end==0) {
	   s = String.format("%s==%s && ",name,objvalue.toString());
	  }
	  else
	  {
		   s = String.format("%s==%s]",name,objvalue.toString());		  
	  }
	  if(last==null)
	  {
		  curr.add(s);
		  writer.print(s);

	  }
	  else
	  {
		  if(!last.contains(s)||SHOW_DELTA==0) {
			  curr.add(s);
			  writer.print(s);
		  }
	  }
  }
  public static void printValue(int end)
  {
	  String s;
	  SHOW_DELTA=0;
	  if(end==0) {
	      s = String.format("%s==%s && ",name,value);
	  }
	  else
	  {
		   s = String.format("%s==%s]",name,value);		  
	  }

	  if(last==null)
	  {
		  curr.add(s);
		  writer.print(s);

	  }
	  else
	  {
		  if(!last.contains(s)||SHOW_DELTA==0) {
			  curr.add(s);
			  writer.print(s);
		  }
		  
	  }
  }
  public static void finish()
  {
	  if(writer!=null)
	  {
		writer.println("\n}");
		writer.flush();
	 	writer.close();
	  }
  }
  public static void printer(String a)
  {
	  if(writer!=null)
	  {
		  last=curr;
		  writer.print("\n\t-> "+a);
	  }
  }

public static int return1() {
	// TODO Auto-generated method stub
	return 1;
}

}
