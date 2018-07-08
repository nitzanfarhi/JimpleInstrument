import java.util.ArrayList;
import java.util.List;

import soot.Body;
import soot.Local;
import soot.PrimType;
import soot.Scene;
import soot.SootClass;
import soot.SootMethod;
import soot.Type;
import soot.Unit;
import soot.Value;
import soot.jimple.AssignStmt;
import soot.jimple.IntConstant;
import soot.jimple.Jimple;
import soot.jimple.NullConstant;

public class Helper {

	 private void constructNewObject(Body b, Type localType, SootMethod constructor) {
	        // "new" statement
	        Value lvalue = getLocalWithName(b, makeLocalName(localType), localType);
	        Value rvalue = Jimple.v().newNewExpr(
	                constructor.getDeclaringClass().getType());
	        AssignStmt ass = Jimple.v().newAssignStmt(lvalue, rvalue);
	        b.getUnits().add(ass);
	        // <init> invocation statement
	        List<Value> args = new ArrayList<Value>();
	        for (Type argt : (List<Type>) constructor.getParameterTypes()) {
	            if (argt instanceof PrimType) {
	                args.add(IntConstant.v(0));
	            } else {
	                args.add(getLocalWithName(b, makeLocalName(argt), argt));
	            }
	        }
	        Value invokeExpr = null;
	        Unit u = null;
	        if (constructor.isStatic()) {
	        	invokeExpr = Jimple.v().newStaticInvokeExpr(constructor.makeRef(), args);
	        	u = Jimple.v().newAssignStmt(lvalue, invokeExpr);
	        } else {
	        	invokeExpr = Jimple.v().newSpecialInvokeExpr((Local) lvalue,
	                constructor.makeRef(), args);
	        	u = Jimple.v().newInvokeStmt(invokeExpr);
	        }
	         
	        b.getUnits().add(u);
	    }


    private String makeLocalName(Type localType) {
        return localType.toString().replaceAll("\\.", "")
                .replaceAll("\\$", "__");
    }
	private Value getLocalWithName(Body b, String name, Type t) {
        for (Local l : b.getLocals()) {
            if (l.getName().equals(name))
                return l;
        }

        // local not found, create one
        Local l = Jimple.v().newLocal(name, t);
        b.getLocals().add(l);
        SootClass sc = Scene.v().getSootClass(t.toString());
        SootMethod constructor = null;
        for (SootMethod sm : sc.getMethods()) {
            if (sm.isConstructor()) {
                constructor = sm;
                break;
            }
        }

        if (constructor != null) {
            System.out.println(" [-] constructing new local with constructor '" + constructor);
            constructNewObject(b, t, constructor);
            return l;
        } else {

            String localNames = "\n";
            for (Local lo : b.getLocals()) {
                localNames += lo.getName() + "  type: " + lo.getType() + " \n";
            }
            System.out.println("[Warning!] no local found with name '" + name + "'" + localNames
                    + " No constructor found for type '" + t + "' returning NullConstant!");
            return NullConstant.v();
        }
    }
	
}
