import bgu.cs.util.Matcher.Case;
import bgu.cs.util.soot.*;
import soot.Unit;

public class myMatcher {

	public static String match(Case<Unit> matchedCase) {
		if(matchedCase == null)
			return "";
		System.out.println(matchedCase.getClass().getSimpleName());
		if(matchedCase instanceof CaseGotoStmt)
			return "";
		else if(matchedCase instanceof CaseIfEq)
			return "";
		if(matchedCase instanceof CaseAssignLocal_BinopExpr) {
			//WHY?
			CaseAssignLocal m = (CaseAssignLocal) (matchedCase);
			String right = m.rhs.toString().replace("$", "");
			String left = m.lhs.toString().replace("$", "");
			return left+" = "+right;
		}
		if(matchedCase instanceof CaseAssignLocal_Invoke) {
			CaseAssignLocal m = (CaseAssignLocal) (matchedCase);
			String right = m.rhs.toString().replace("$", "");
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
		

		else if(matchedCase instanceof CaseReturnStmt)
		{
			return matchedCase.toString();			
		}

		return "";
	}

}
