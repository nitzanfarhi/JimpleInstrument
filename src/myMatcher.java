import bgu.cs.util.Matcher.Case;
import bgu.cs.util.soot.*;
import soot.AbstractSootFieldRef;
import soot.Unit;
import soot.Value;
import soot.jimple.internal.JInstanceFieldRef;

public class myMatcher {

	public static String match(Case<Unit> matchedCase) {
		if(matchedCase == null)
			return "";
//		if(matchedCase instanceof CaseGotoStmt)
//			return "";
//		else if(matchedCase instanceof CaseIfEq)
//			return "";
		
		if(matchedCase instanceof CaseAssignLocal_Invoke) {
			CaseAssignLocal_Invoke m = (CaseAssignLocal_Invoke) (matchedCase);
			String right = m.methodName+"(";
			for(int i=0;i<m.args.size();i++) {
				right+=m.args.get(i);
				if(i<m.args.size()-1)right+=", ";
			}
			right+=")";
			String left = m.lhs.toString().replace("$", "");
			return left+" = "+right;
		}
		if(matchedCase instanceof CaseAssignLocal_InstanceFieldRef) {
			CaseAssignLocal_InstanceFieldRef m = (CaseAssignLocal_InstanceFieldRef) (matchedCase);
			String right = m.base.getName().replace("$", "")+"."+m.instanceFieldRef.getFieldRef().name();
			String left = m.lhs.toString().replace("$", "");
			return left+" = "+right;
		}
		if(matchedCase instanceof CaseAssignInstanceFieldRef) {
			CaseAssignInstanceFieldRef m = (CaseAssignInstanceFieldRef) (matchedCase);
			String left = m.base.getName().replace("$", "")+"."+m.instanceFieldRef.getField().getName();
			String right = m.rhs.toString().replace("$", "");
			return left+" = "+right;
		}
		if(matchedCase instanceof CaseAssignLocal_NewExpr) {//new ..
			CaseAssignLocal_NewExpr m = (CaseAssignLocal_NewExpr) matchedCase;
			String right = m.rhs.toString().replace("$", "");
			if(m.rhs instanceof JInstanceFieldRef)
				right = ((JInstanceFieldRef)m.rhs).getBaseBox().getValue()+
						((JInstanceFieldRef)m.rhs).getFieldRef().name();
			String left = m.lhs.toString().replace("$", "");
			return left+" = "+right;
		}
		if(matchedCase instanceof CaseAssignStaticFieldRef) {
			CaseAssignStaticFieldRef m = (CaseAssignStaticFieldRef) (matchedCase);
			String right = m.assign.getRightOpBox().getValue().toString();
			String left = m.assign.getFieldRef().toString();
//			String right = ((JInstanceFieldRef)m.rhs).getBaseBox().getValue()+"."+
//						((JInstanceFieldRef)m.rhs).getFieldRef().name();
//			String left = m.lhs.toString().replace("$", "");
			return left+" = "+right;
		}

		if(matchedCase instanceof CaseAssignLocal) {
			CaseAssignLocal m = (CaseAssignLocal) (matchedCase);
			String right = m.rhs.toString().replace("$", "");
			if(m.rhs instanceof JInstanceFieldRef)
				right = ((JInstanceFieldRef)m.rhs).getBaseBox().getValue()+"."+
						((JInstanceFieldRef)m.rhs).getFieldRef().name();
			String left = m.lhs.toString().replace("$", "");
			return left+" = "+right;
		}
		
		
//		else if(matchedCase instanceof CaseAssignLocal)
//		{
//			CaseAssignLocal m = (CaseAssignLocal) (matchedCase);
//			String right = m.rhs.toString().replace("$", "");
//			String left = m.lhs.toString().replace("$", "");
//			//if(m.rhs.getUseBoxes().size()>0)
//			//	right = m.rhs.getUseBoxes().get(0).getValue().toString().replace("$", "");
//			//if(m.lhs.getUseBoxes().size()>0)
//			//	left = m.lhs.getUseBoxes().get(0).getValue().toString().replace("$", "");
//			//String left = m.lhs.getUseBoxes().get(0).getValue()+"";
//			//String left="";
//			//return m.assign.toString().replace("$", "");
//			return left+" = "+right;
//		//	return left+" = "+right;
//		}
		
		System.out.println("**** "+ matchedCase.getClass().getSimpleName());
		if(matchedCase instanceof CaseReturnStmt)
		{
			return matchedCase.toString();			
		}

		return "";
	}

}
