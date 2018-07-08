import bgu.cs.util.Matcher.Case;
import bgu.cs.util.soot.*;
import soot.Unit;

public class myMatcher {

	public static String match(Case<Unit> matchedCase) {
		if(matchedCase == null)
			return "";
		else if(matchedCase instanceof CaseGotoStmt)
			return "";
		else if(matchedCase instanceof CaseIfEq)
			return "";
		else if(matchedCase instanceof CaseAssignLocal)
		{
			CaseAssignLocal m = (CaseAssignLocal) (matchedCase);
			return m.assign.toString();
		}
		else if(matchedCase instanceof CaseAssignLocal_BinopExpr)
		{
			return matchedCase.toString();	
		}	
		else if(matchedCase instanceof CaseReturnStmt)
		{
			return matchedCase.toString();			
		}

		return "";
	}

}
