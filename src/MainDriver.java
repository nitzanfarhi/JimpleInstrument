import soot.*;
import soot.options.Options;

import java.io.File;
import java.util.Arrays;

/**
 * Created by mian on 6/22/16.
 * https://www.sable.mcgill.ca/soot/tutorial/   More on profiling
 * argument example: TestInvoke
 */
public class MainDriver {
	public static boolean DELTA=false;
    public static void main(String[] args) {

        /* check the arguments */
    	System.out.println("Compiled Helper: "+MyCounter.return1());
        if (args.length == 0) {
            System.err.println("Usage: java MainDriver classname [options]");
            System.err.println("options:");
            System.err.println("-d : trace delta");
            
            System.exit(0);
        }
        for(int i=0;i<args.length;i++)
        {
        	if(args[i].equals("-d"))
        	{
        		System.out.println("ENABLED");
        		DELTA=true;
        	}
        		
        }
        
       String s = Scene.v().getSootClassPath() + File.pathSeparator + "C:\\Users\\admin\\eclipse-workspace\\JimpInstrument\\bin";      
       Scene.v().setSootClassPath(s);

       Pack jtp = PackManager.v().getPack("jtp");
       jtp.add(new Transform("jtp.instrumenter",
                             new InvokeStaticInstrumenter()));

       String[] args2 = new String[2];
       args2[0]=args[0];
       args2[1]="MyCounter";
       soot.Main.main(args2);
    }
}