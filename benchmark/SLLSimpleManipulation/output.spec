type SLL {
  d:int
  l:SLL
  r:SLL
}

SLLSimpleManipulation (mut r0:SLL) -> (res:int){
	var loc_SLL:SLL

	example {[r0==o0 && o0.d==0 && o0.l==null && o0.r==null]
	-> loc_SLL = r0;
	-> loc_SLL.d = 3;//r0.d==3 && r0.l==null && r0.r==null
	}

}
