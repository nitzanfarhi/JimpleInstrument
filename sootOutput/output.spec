type SLL {
  d:int
  l:SLL
  r:SLL
}

goo (mut r0:SLL,mut r1:SLL,mut r2:SLL,mut r3:SLL,mut r4:SLL,mut i5:int) -> (res:int){
	example {[r0.d==0 && r0.l==null && r0.r==null && r1.d==2 && r1.l==null && r1.r==null && r2.d==3 && r2.l==null && r2.r==null && r3.d==4 && r3.l==null && r3.r==null && r4.d==5 && r4.l==null && r4.r==null && i4==3]
	-> i5 = 33;//$i0==0 && $i1==0 && $i2==0 && $i3==0 && i4==3 && i5==33 && r5==null]
	-> r1.d = 13;//r1.d==13 && r1.l==null && r1.r==null && 
	-> r2.d = 12;//r2.d==12 && r2.l==null && r2.r==null && 
	-> r3.d = 11;//r3.d==11 && r3.l==null && r3.r==null && 
	-> r4.d = 10;//r4.d==10 && r4.l==null && r4.r==null && 
	-> r1.l = r2;//r1.d==13 && r1.l==r2 && r1.r==null && 
	-> r2.l = r3;//r2.d==12 && r2.l==r3 && r2.r==null && 
	-> r3.l = r4;//r3.d==11 && r3.l==r4 && r3.r==null && 
	-> r5 = r1;//r5.d==13]r5.l==r2]r5.r==null]
	-> i5 = i5 + 1;//i5==34 && 
	-> i0 = r5.d;//$i0==13 && 
	-> r5 = r5.l;//r5.d==12]r5.l==r3]r5.r==null]
	-> i4 = i4 + -1;//i4==2 && 
	-> i5 = i5 + 1;//i5==35 && 
	-> i0 = r5.d;//$i0==12 && 
	-> r5 = r5.l;//r5.d==11]r5.l==r4]r5.r==null]
	-> i4 = i4 + -1;//i4==1 && 
	-> i5 = i5 + 1;//i5==36 && 
	-> i0 = r5.d;//$i0==11 && 
	-> r5 = r5.l;//r5.d==10]r5.l==null]r5.r==null]
	-> i4 = i4 + -1;//i4==0 && 
	-> i5 = i5 + 1;//i5==37 && 
	-> i0 = r5.d;//$i0==10 && 
	-> r5 = r5.l;//
	-> i4 = i4 + -1;//i4==-1 && 
	}
	example {[r0.d==0 && r0.l==null && r0.r==null && r1.d==2 && r1.l==null && r1.r==null && r2.d==3 && r2.l==null && r2.r==null && r3.d==4 && r3.l==null && r3.r==null && r4.d==5 && r4.l==null && r4.r==null && i4==3]
	-> i5 = 33;//$i0==0 && $i1==0 && $i2==0 && $i3==0 && i4==3 && i5==33 && r5==null]
	-> r1.d = 13;//r1.d==13 && r1.l==null && r1.r==null && 
	-> r2.d = 12;//r2.d==12 && r2.l==null && r2.r==null && 
	-> r3.d = 11;//r3.d==11 && r3.l==null && r3.r==null && 
	-> r4.d = 10;//r4.d==10 && r4.l==null && r4.r==null && 
	-> r1.l = r2;//r1.d==13 && r1.l==r2 && r1.r==null && 
	-> r2.l = r3;//r2.d==12 && r2.l==r3 && r2.r==null && 
	-> r3.l = r4;//r3.d==11 && r3.l==r4 && r3.r==null && 
	-> r5 = r1;//r5.d==13]r5.l==r2]r5.r==null]
	-> i5 = i5 + 1;//i5==34 && 
	-> i0 = r5.d;//$i0==13 && 
	-> r5 = r5.l;//r5.d==12]r5.l==r3]r5.r==null]
	-> i4 = i4 + -1;//i4==2 && 
	-> i5 = i5 + 1;//i5==35 && 
	-> i0 = r5.d;//$i0==12 && 
	-> r5 = r5.l;//r5.d==11]r5.l==r4]r5.r==null]
	-> i4 = i4 + -1;//i4==1 && 
	-> i5 = i5 + 1;//i5==36 && 
	-> i0 = r5.d;//$i0==11 && 
	-> r5 = r5.l;//r5.d==10]r5.l==null]r5.r==null]
	-> i4 = i4 + -1;//i4==0 && 
	-> i5 = i5 + 1;//i5==37 && 
	-> i0 = r5.d;//$i0==10 && 
	-> r5 = r5.l;//
	-> i4 = i4 + -1;//i4==-1 && 
	}
	example {[r0.d==0 && r0.l==null && r0.r==null && r1.d==2 && r1.l==null && r1.r==null && r2.d==3 && r2.l==null && r2.r==null && r3.d==4 && r3.l==null && r3.r==null && r4.d==5 && r4.l==null && r4.r==null && i4==3]
	-> i5 = 33;//$i0==0 && $i1==0 && $i2==0 && $i3==0 && i4==3 && i5==33 && r5==null]
	-> r1.d = 13;//r1.d==13 && r1.l==null && r1.r==null && 
	-> r2.d = 12;//r2.d==12 && r2.l==null && r2.r==null && 
	-> r3.d = 11;//r3.d==11 && r3.l==null && r3.r==null && 
	-> r4.d = 10;//r4.d==10 && r4.l==null && r4.r==null && 
	-> r1.l = r2;//r1.d==13 && r1.l==r2 && r1.r==null && 
	-> r2.l = r3;//r2.d==12 && r2.l==r3 && r2.r==null && 
	-> r3.l = r4;//r3.d==11 && r3.l==r4 && r3.r==null && 
	-> r5 = r1;//r5.d==13]r5.l==r2]r5.r==null]
	-> i5 = i5 + 1;//i5==34 && 
	-> i0 = r5.d;//$i0==13 && 
	-> r5 = r5.l;//r5.d==12]r5.l==r3]r5.r==null]
	-> i4 = i4 + -1;//i4==2 && 
	-> i5 = i5 + 1;//i5==35 && 
	-> i0 = r5.d;//$i0==12 && 
	-> r5 = r5.l;//r5.d==11]r5.l==r4]r5.r==null]
	-> i4 = i4 + -1;//i4==1 && 
	-> i5 = i5 + 1;//i5==36 && 
	-> i0 = r5.d;//$i0==11 && 
	-> r5 = r5.l;//r5.d==10]r5.l==null]r5.r==null]
	-> i4 = i4 + -1;//i4==0 && 
	-> i5 = i5 + 1;//i5==37 && 
	-> i0 = r5.d;//$i0==10 && 
	-> r5 = r5.l;//
	-> i4 = i4 + -1;//i4==-1 && 
	}
	example {[r0.d==0 && r0.l==null && r0.r==null && r1.d==2 && r1.l==null && r1.r==null && r2.d==3 && r2.l==null && r2.r==null && r3.d==4 && r3.l==null && r3.r==null && r4.d==5 && r4.l==null && r4.r==null && i4==3]
	-> i5 = 33;//$i0==0 && $i1==0 && $i2==0 && $i3==0 && i4==3 && i5==33 && r5==null]
	-> r1.d = 13;//r1.d==13 && r1.l==null && r1.r==null && 
	-> r2.d = 12;//r2.d==12 && r2.l==null && r2.r==null && 
	-> r3.d = 11;//r3.d==11 && r3.l==null && r3.r==null && 
	-> r4.d = 10;//r4.d==10 && r4.l==null && r4.r==null && 
	-> r1.l = r2;//r1.d==13 && r1.l==r2 && r1.r==null && 
	-> r2.l = r3;//r2.d==12 && r2.l==r3 && r2.r==null && 
	-> r3.l = r4;//r3.d==11 && r3.l==r4 && r3.r==null && 
	-> r5 = r1;//r5.d==13]r5.l==r2]r5.r==null]
	-> i5 = i5 + 1;//i5==34 && 
	-> i0 = r5.d;//$i0==13 && 
	-> r5 = r5.l;//r5.d==12]r5.l==r3]r5.r==null]
	-> i4 = i4 + -1;//i4==2 && 
	-> i5 = i5 + 1;//i5==35 && 
	-> i0 = r5.d;//$i0==12 && 
	-> r5 = r5.l;//r5.d==11]r5.l==r4]r5.r==null]
	-> i4 = i4 + -1;//i4==1 && 
	-> i5 = i5 + 1;//i5==36 && 
	-> i0 = r5.d;//$i0==11 && 
	-> r5 = r5.l;//r5.d==10]r5.l==null]r5.r==null]
	-> i4 = i4 + -1;//i4==0 && 
	-> i5 = i5 + 1;//i5==37 && 
	-> i0 = r5.d;//$i0==10 && 
	-> r5 = r5.l;//
	-> i4 = i4 + -1;//i4==-1 && 
	}
	example {[r0.d==0 && r0.l==null && r0.r==null && r1.d==2 && r1.l==null && r1.r==null && r2.d==3 && r2.l==null && r2.r==null && r3.d==4 && r3.l==null && r3.r==null && r4.d==5 && r4.l==null && r4.r==null && i4==3]
	-> i5 = 33;//$i0==0 && $i1==0 && $i2==0 && $i3==0 && i4==3 && i5==33 && r5==null]
	-> r1.d = 13;//r1.d==13 && r1.l==null && r1.r==null && 
	-> r2.d = 12;//r2.d==12 && r2.l==null && r2.r==null && 
	-> r3.d = 11;//r3.d==11 && r3.l==null && r3.r==null && 
	-> r4.d = 10;//r4.d==10 && r4.l==null && r4.r==null && 
	-> r1.l = r2;//r1.d==13 && r1.l==r2 && r1.r==null && 
	-> r2.l = r3;//r2.d==12 && r2.l==r3 && r2.r==null && 
	-> r3.l = r4;//r3.d==11 && r3.l==r4 && r3.r==null && 
	-> r5 = r1;//r5.d==13]r5.l==r2]r5.r==null]
	-> i5 = i5 + 1;//i5==34 && 
	-> i0 = r5.d;//$i0==13 && 
	-> r5 = r5.l;//r5.d==12]r5.l==r3]r5.r==null]
	-> i4 = i4 + -1;//i4==2 && 
	-> i5 = i5 + 1;//i5==35 && 
	-> i0 = r5.d;//$i0==12 && 
	-> r5 = r5.l;//r5.d==11]r5.l==r4]r5.r==null]
	-> i4 = i4 + -1;//i4==1 && 
	-> i5 = i5 + 1;//i5==36 && 
	-> i0 = r5.d;//$i0==11 && 
	-> r5 = r5.l;//r5.d==10]r5.l==null]r5.r==null]
	-> i4 = i4 + -1;//i4==0 && 
	-> i5 = i5 + 1;//i5==37 && 
	-> i0 = r5.d;//$i0==10 && 
	-> r5 = r5.l;//
	-> i4 = i4 + -1;//i4==-1 && 
	}
	example {[r0.d==0 && r0.l==null && r0.r==null && r1.d==2 && r1.l==null && r1.r==null && r2.d==3 && r2.l==null && r2.r==null && r3.d==4 && r3.l==null && r3.r==null && r4.d==5 && r4.l==null && r4.r==null && i4==3]
	-> i5 = 33;//$i0==0 && $i1==0 && $i2==0 && $i3==0 && i4==3 && i5==33 && r5==null]
	-> r1.d = 13;//r1.d==13 && r1.l==null && r1.r==null && 
	-> r2.d = 12;//r2.d==12 && r2.l==null && r2.r==null && 
	-> r3.d = 11;//r3.d==11 && r3.l==null && r3.r==null && 
	-> r4.d = 10;//r4.d==10 && r4.l==null && r4.r==null && 
	-> r1.l = r2;//r1.d==13 && r1.l==r2 && r1.r==null && 
	-> r2.l = r3;//r2.d==12 && r2.l==r3 && r2.r==null && 
	-> r3.l = r4;//r3.d==11 && r3.l==r4 && r3.r==null && 
	-> r5 = r1;//r5.d==13]r5.l==r2]r5.r==null]
	-> i5 = i5 + 1;//i5==34 && 
	-> i0 = r5.d;//$i0==13 && 
	-> r5 = r5.l;//r5.d==12]r5.l==r3]r5.r==null]
	-> i4 = i4 + -1;//i4==2 && 
	-> i5 = i5 + 1;//i5==35 && 
	-> i0 = r5.d;//$i0==12 && 
	-> r5 = r5.l;//r5.d==11]r5.l==r4]r5.r==null]
	-> i4 = i4 + -1;//i4==1 && 
	-> i5 = i5 + 1;//i5==36 && 
	-> i0 = r5.d;//$i0==11 && 
	-> r5 = r5.l;//r5.d==10]r5.l==null]r5.r==null]
	-> i4 = i4 + -1;//i4==0 && 
	-> i5 = i5 + 1;//i5==37 && 
	-> i0 = r5.d;//$i0==10 && 
	-> r5 = r5.l;//
	-> i4 = i4 + -1;//i4==-1 && 
	}
	example {[r0.d==0 && r0.l==null && r0.r==null && r1.d==2 && r1.l==null && r1.r==null && r2.d==3 && r2.l==null && r2.r==null && r3.d==4 && r3.l==null && r3.r==null && r4.d==5 && r4.l==null && r4.r==null && i4==3]
	-> i5 = 33;//$i0==0 && $i1==0 && $i2==0 && $i3==0 && i4==3 && i5==33 && r5==null]
	-> r1.d = 13;//r1.d==13 && r1.l==null && r1.r==null && 
	-> r2.d = 12;//r2.d==12 && r2.l==null && r2.r==null && 
	-> r3.d = 11;//r3.d==11 && r3.l==null && r3.r==null && 
	-> r4.d = 10;//r4.d==10 && r4.l==null && r4.r==null && 
	-> r1.l = r2;//r1.d==13 && r1.l==r2 && r1.r==null && 
	-> r2.l = r3;//r2.d==12 && r2.l==r3 && r2.r==null && 
	-> r3.l = r4;//r3.d==11 && r3.l==r4 && r3.r==null && 
	-> r5 = r1;//r5.d==13]r5.l==r2]r5.r==null]
	-> i5 = i5 + 1;//i5==34 && 
	-> i0 = r5.d;//$i0==13 && 
	-> r5 = r5.l;//r5.d==12]r5.l==r3]r5.r==null]
	-> i4 = i4 + -1;//i4==2 && 
	-> i5 = i5 + 1;//i5==35 && 
	-> i0 = r5.d;//$i0==12 && 
	-> r5 = r5.l;//r5.d==11]r5.l==r4]r5.r==null]
	-> i4 = i4 + -1;//i4==1 && 
	-> i5 = i5 + 1;//i5==36 && 
	-> i0 = r5.d;//$i0==11 && 
	-> r5 = r5.l;//r5.d==10]r5.l==null]r5.r==null]
	-> i4 = i4 + -1;//i4==0 && 
	-> i5 = i5 + 1;//i5==37 && 
	-> i0 = r5.d;//$i0==10 && 
	-> r5 = r5.l;//
	-> i4 = i4 + -1;//i4==-1 && 
	}
	example {[r0.d==0 && r0.l==null && r0.r==null && r1.d==2 && r1.l==null && r1.r==null && r2.d==3 && r2.l==null && r2.r==null && r3.d==4 && r3.l==null && r3.r==null && r4.d==5 && r4.l==null && r4.r==null && i4==3]
	-> i5 = 33;//$i0==0 && $i1==0 && $i2==0 && $i3==0 && i4==3 && i5==33 && r5==null]
	-> r1.d = 13;//r1.d==13 && r1.l==null && r1.r==null && 
	-> r2.d = 12;//r2.d==12 && r2.l==null && r2.r==null && 
	-> r3.d = 11;//r3.d==11 && r3.l==null && r3.r==null && 
	-> r4.d = 10;//r4.d==10 && r4.l==null && r4.r==null && 
	-> r1.l = r2;//r1.d==13 && r1.l==r2 && r1.r==null && 
	-> r2.l = r3;//r2.d==12 && r2.l==r3 && r2.r==null && 
	-> r3.l = r4;//r3.d==11 && r3.l==r4 && r3.r==null && 
	-> r5 = r1;//r5.d==13]r5.l==r2]r5.r==null]
	-> i5 = i5 + 1;//i5==34 && 
	-> i0 = r5.d;//$i0==13 && 
	-> r5 = r5.l;//r5.d==12]r5.l==r3]r5.r==null]
	-> i4 = i4 + -1;//i4==2 && 
	-> i5 = i5 + 1;//i5==35 && 
	-> i0 = r5.d;//$i0==12 && 
	-> r5 = r5.l;//r5.d==11]r5.l==r4]r5.r==null]
	-> i4 = i4 + -1;//i4==1 && 
	-> i5 = i5 + 1;//i5==36 && 
	-> i0 = r5.d;//$i0==11 && 
	-> r5 = r5.l;//r5.d==10]r5.l==null]r5.r==null]
	-> i4 = i4 + -1;//i4==0 && 
	-> i5 = i5 + 1;//i5==37 && 
	-> i0 = r5.d;//$i0==10 && 
	-> r5 = r5.l;//
	-> i4 = i4 + -1;//i4==-1 && 
	}
	example {[r0.d==0 && r0.l==null && r0.r==null && r1.d==2 && r1.l==null && r1.r==null && r2.d==3 && r2.l==null && r2.r==null && r3.d==4 && r3.l==null && r3.r==null && r4.d==5 && r4.l==null && r4.r==null && i4==3]
	-> i5 = 33;//$i0==0 && $i1==0 && $i2==0 && $i3==0 && i4==3 && i5==33 && r5==null]
	-> r1.d = 13;//r1.d==13 && r1.l==null && r1.r==null && 
	-> r2.d = 12;//r2.d==12 && r2.l==null && r2.r==null && 
	-> r3.d = 11;//r3.d==11 && r3.l==null && r3.r==null && 
	-> r4.d = 10;//r4.d==10 && r4.l==null && r4.r==null && 
	-> r1.l = r2;//r1.d==13 && r1.l==r2 && r1.r==null && 
	-> r2.l = r3;//r2.d==12 && r2.l==r3 && r2.r==null && 
	-> r3.l = r4;//r3.d==11 && r3.l==r4 && r3.r==null && 
	-> r5 = r1;//r5.d==13]r5.l==r2]r5.r==null]
	-> i5 = i5 + 1;//i5==34 && 
	-> i0 = r5.d;//$i0==13 && 
	-> r5 = r5.l;//r5.d==12]r5.l==r3]r5.r==null]
	-> i4 = i4 + -1;//i4==2 && 
	-> i5 = i5 + 1;//i5==35 && 
	-> i0 = r5.d;//$i0==12 && 
	-> r5 = r5.l;//r5.d==11]r5.l==r4]r5.r==null]
	-> i4 = i4 + -1;//i4==1 && 
	-> i5 = i5 + 1;//i5==36 && 
	-> i0 = r5.d;//$i0==11 && 
	-> r5 = r5.l;//r5.d==10]r5.l==null]r5.r==null]
	-> i4 = i4 + -1;//i4==0 && 
	-> i5 = i5 + 1;//i5==37 && 
	-> i0 = r5.d;//$i0==10 && 
	-> r5 = r5.l;//
	-> i4 = i4 + -1;//i4==-1 && 
	}
	example {[r0.d==0 && r0.l==null && r0.r==null && r1.d==2 && r1.l==null && r1.r==null && r2.d==3 && r2.l==null && r2.r==null && r3.d==4 && r3.l==null && r3.r==null && r4.d==5 && r4.l==null && r4.r==null && i4==3]
	-> i5 = 33;//$i0==0 && $i1==0 && $i2==0 && $i3==0 && i4==3 && i5==33 && r5==null]
	-> r1.d = 13;//r1.d==13 && r1.l==null && r1.r==null && 
	-> r2.d = 12;//r2.d==12 && r2.l==null && r2.r==null && 
	-> r3.d = 11;//r3.d==11 && r3.l==null && r3.r==null && 
	-> r4.d = 10;//r4.d==10 && r4.l==null && r4.r==null && 
	-> r1.l = r2;//r1.d==13 && r1.l==r2 && r1.r==null && 
	-> r2.l = r3;//r2.d==12 && r2.l==r3 && r2.r==null && 
	-> r3.l = r4;//r3.d==11 && r3.l==r4 && r3.r==null && 
	-> r5 = r1;//r5.d==13]r5.l==r2]r5.r==null]
	-> i5 = i5 + 1;//i5==34 && 
	-> i0 = r5.d;//$i0==13 && 
	-> r5 = r5.l;//r5.d==12]r5.l==r3]r5.r==null]
	-> i4 = i4 + -1;//i4==2 && 
	-> i5 = i5 + 1;//i5==35 && 
	-> i0 = r5.d;//$i0==12 && 
	-> r5 = r5.l;//r5.d==11]r5.l==r4]r5.r==null]
	-> i4 = i4 + -1;//i4==1 && 
	-> i5 = i5 + 1;//i5==36 && 
	-> i0 = r5.d;//$i0==11 && 
	-> r5 = r5.l;//r5.d==10]r5.l==null]r5.r==null]
	-> i4 = i4 + -1;//i4==0 && 
	-> i5 = i5 + 1;//i5==37 && 
	-> i0 = r5.d;//$i0==10 && 
	-> r5 = r5.l;//
	-> i4 = i4 + -1;//i4==-1 && 
	}
	example {[r0.d==0 && r0.l==null && r0.r==null && r1.d==2 && r1.l==null && r1.r==null && r2.d==3 && r2.l==null && r2.r==null && r3.d==4 && r3.l==null && r3.r==null && r4.d==5 && r4.l==null && r4.r==null && i4==3]
	-> i5 = 33;//$i0==0 && $i1==0 && $i2==0 && $i3==0 && i4==3 && i5==33 && r5==null]
	-> r1.d = 13;//r1.d==13 && r1.l==null && r1.r==null && 
	-> r2.d = 12;//r2.d==12 && r2.l==null && r2.r==null && 
	-> r3.d = 11;//r3.d==11 && r3.l==null && r3.r==null && 
	-> r4.d = 10;//r4.d==10 && r4.l==null && r4.r==null && 
	-> r1.l = r2;//r1.d==13 && r1.l==r2 && r1.r==null && 
	-> r2.l = r3;//r2.d==12 && r2.l==r3 && r2.r==null && 
	-> r3.l = r4;//r3.d==11 && r3.l==r4 && r3.r==null && 
	-> r5 = r1;//r5.d==13]r5.l==r2]r5.r==null]
	-> i5 = i5 + 1;//i5==34 && 
	-> i0 = r5.d;//$i0==13 && 
	-> r5 = r5.l;//r5.d==12]r5.l==r3]r5.r==null]
	-> i4 = i4 + -1;//i4==2 && 
	-> i5 = i5 + 1;//i5==35 && 
	-> i0 = r5.d;//$i0==12 && 
	-> r5 = r5.l;//r5.d==11]r5.l==r4]r5.r==null]
	-> i4 = i4 + -1;//i4==1 && 
	-> i5 = i5 + 1;//i5==36 && 
	-> i0 = r5.d;//$i0==11 && 
	-> r5 = r5.l;//r5.d==10]r5.l==null]r5.r==null]
	-> i4 = i4 + -1;//i4==0 && 
	-> i5 = i5 + 1;//i5==37 && 
	-> i0 = r5.d;//$i0==10 && 
	-> r5 = r5.l;//
	-> i4 = i4 + -1;//i4==-1 && 
	}

}
