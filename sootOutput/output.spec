goo (mut i0:SLL,mut i1:SLL,mut i2:SLL,mut i3:SLL,mut i4:SLL,mut i5:int) -> (res:int){
	example {[r0.d==0 && r0.l==null && r0.r==null && r1.d==2 && r1.l==null && r1.r==null && r2.d==3 && r2.l==null && r2.r==null && r3.d==4 && r3.l==null && r3.r==null && r4.d==5 && r4.l==null && r4.r==null && i8==3]
	-> i9 = 33;//$i0==0 && $i1==0 && $i2==0 && $i3==0 && $i4==0 && $i5==0 && $i6==0 && $i7==0 && i8==3 && i9==33 && r5==null]
	-> i0 = <TestInvoke: int a>;//$i0==13 && 
	-> r1.d = r1.d;//r1.d==13 && r1.l==null && r1.r==null && 
	-> i1 = <TestInvoke: int a>;//$i1==12 && 
	-> r2.d = r2.d;//r2.d==12 && r2.l==null && r2.r==null && 
	-> i2 = <TestInvoke: int a>;//$i2==11 && 
	-> r3.d = r3.d;//r3.d==11 && r3.l==null && r3.r==null && 
	-> i3 = <TestInvoke: int a>;//$i3==10 && 
	-> r4.d = r4.d;//r4.d==10 && r4.l==null && r4.r==null && 
	-> r1.l = r1.l;//r1.d==13 && r1.l==r2 && r1.r==null && 
	-> r2.l = r2.l;//r2.d==12 && r2.l==r3 && r2.r==null && 
	-> r3.l = r3.l;//r3.d==11 && r3.l==r4 && r3.r==null && 
	-> r5 = r1;//r5.d==13]r5.l==r2]r5.r==null]
	-> i9 = i9 + 1;//i9==34 && 
	-> i4 = r5.d;//$i4==13 && 
	-> r5 = r5.l;//r5.d==12]r5.l==r3]r5.r==null]
	-> i8 = i8 + -1;//i8==2 && 
	-> i9 = i9 + 1;//i9==35 && 
	-> i4 = r5.d;//$i4==12 && 
	-> r5 = r5.l;//r5.d==11]r5.l==r4]r5.r==null]
	-> i8 = i8 + -1;//i8==1 && 
	-> i9 = i9 + 1;//i9==36 && 
	-> i4 = r5.d;//$i4==11 && 
	-> r5 = r5.l;//r5.d==10]r5.l==null]r5.r==null]
	-> i8 = i8 + -1;//i8==0 && 
	-> i9 = i9 + 1;//i9==37 && 
	-> i4 = r5.d;//$i4==10 && 
	-> r5 = r5.l;//
	-> i8 = i8 + -1;//i8==-1 && 
	}
	example {[
	-> i9 = 33;//r0.d==0 && r0.l==null && r0.r==null && r1.d==2 && r1.l==null && r1.r==null && r2.d==3 && r2.l==null && r2.r==null && r3.d==4 && r3.l==null && r3.r==null && r4.d==5 && r4.l==null && r4.r==null && $i0==0 && $i1==0 && $i2==0 && $i3==0 && $i4==0 && $i5==0 && $i6==0 && $i7==0 && i8==3 && i9==33 && r5==null]
	-> i0 = <TestInvoke: int a>;//$i0==13 && 
	-> r1.d = r1.d;//r1.d==13 && r1.l==null && r1.r==null && 
	-> i1 = <TestInvoke: int a>;//$i1==12 && 
	-> r2.d = r2.d;//r2.d==12 && r2.l==null && r2.r==null && 
	-> i2 = <TestInvoke: int a>;//$i2==11 && 
	-> r3.d = r3.d;//r3.d==11 && r3.l==null && r3.r==null && 
	-> i3 = <TestInvoke: int a>;//$i3==10 && 
	-> r4.d = r4.d;//r4.d==10 && r4.l==null && r4.r==null && 
	-> r1.l = r1.l;//r1.d==13 && r1.l==r2 && r1.r==null && 
	-> r2.l = r2.l;//r2.d==12 && r2.l==r3 && r2.r==null && 
	-> r3.l = r3.l;//r3.d==11 && r3.l==r4 && r3.r==null && 
	-> r5 = r1;//r5.d==13]r5.l==r2]r5.r==null]
	-> i9 = i9 + 1;//i9==34 && 
	-> i4 = r5.d;//$i4==13 && 
	-> r5 = r5.l;//r5.d==12]r5.l==r3]r5.r==null]
	-> i8 = i8 + -1;//i8==2 && 
	-> i9 = i9 + 1;//i9==35 && 
	-> i4 = r5.d;//$i4==12 && 
	-> r5 = r5.l;//r5.d==11]r5.l==r4]r5.r==null]
	-> i8 = i8 + -1;//i8==1 && 
	-> i9 = i9 + 1;//i9==36 && 
	-> i4 = r5.d;//$i4==11 && 
	-> r5 = r5.l;//r5.d==10]r5.l==null]r5.r==null]
	-> i8 = i8 + -1;//i8==0 && 
	-> i9 = i9 + 1;//i9==37 && 
	-> i4 = r5.d;//$i4==10 && 
	-> r5 = r5.l;//
	-> i8 = i8 + -1;//i8==-1 && 
	}
	example {[i8==3]
	-> i9 = 33;//r0.d==0 && r0.l==null && r0.r==null && r1.d==2 && r1.l==null && r1.r==null && r2.d==3 && r2.l==null && r2.r==null && r3.d==4 && r3.l==null && r3.r==null && r4.d==5 && r4.l==null && r4.r==null && $i0==0 && $i1==0 && $i2==0 && $i3==0 && $i4==0 && $i5==0 && $i6==0 && $i7==0 && i8==3 && i9==33 && r5==null]
	-> i0 = <TestInvoke: int a>;//$i0==13 && 
	-> r1.d = r1.d;//r1.d==13 && r1.l==null && r1.r==null && 
	-> i1 = <TestInvoke: int a>;//$i1==12 && 
	-> r2.d = r2.d;//r2.d==12 && r2.l==null && r2.r==null && 
	-> i2 = <TestInvoke: int a>;//$i2==11 && 
	-> r3.d = r3.d;//r3.d==11 && r3.l==null && r3.r==null && 
	-> i3 = <TestInvoke: int a>;//$i3==10 && 
	-> r4.d = r4.d;//r4.d==10 && r4.l==null && r4.r==null && 
	-> r1.l = r1.l;//r1.d==13 && r1.l==r2 && r1.r==null && 
	-> r2.l = r2.l;//r2.d==12 && r2.l==r3 && r2.r==null && 
	-> r3.l = r3.l;//r3.d==11 && r3.l==r4 && r3.r==null && 
	-> r5 = r1;//r5.d==13]r5.l==r2]r5.r==null]
	-> i9 = i9 + 1;//i9==34 && 
	-> i4 = r5.d;//$i4==13 && 
	-> r5 = r5.l;//r5.d==12]r5.l==r3]r5.r==null]
	-> i8 = i8 + -1;//i8==2 && 
	-> i9 = i9 + 1;//i9==35 && 
	-> i4 = r5.d;//$i4==12 && 
	-> r5 = r5.l;//r5.d==11]r5.l==r4]r5.r==null]
	-> i8 = i8 + -1;//i8==1 && 
	-> i9 = i9 + 1;//i9==36 && 
	-> i4 = r5.d;//$i4==11 && 
	-> r5 = r5.l;//r5.d==10]r5.l==null]r5.r==null]
	-> i8 = i8 + -1;//i8==0 && 
	-> i9 = i9 + 1;//i9==37 && 
	-> i4 = r5.d;//$i4==10 && 
	-> r5 = r5.l;//
	-> i8 = i8 + -1;//i8==-1 && 
	}
	example {[
	-> i9 = 33;//r0.d==0 && r0.l==null && r0.r==null && r1.d==2 && r1.l==null && r1.r==null && r2.d==3 && r2.l==null && r2.r==null && r3.d==4 && r3.l==null && r3.r==null && r4.d==5 && r4.l==null && r4.r==null && $i0==0 && $i1==0 && $i2==0 && $i3==0 && $i4==0 && $i5==0 && $i6==0 && $i7==0 && i8==3 && i9==33 && r5==null]
	-> i0 = <TestInvoke: int a>;//$i0==13 && 
	-> r1.d = r1.d;//r1.d==13 && r1.l==null && r1.r==null && 
	-> i1 = <TestInvoke: int a>;//$i1==12 && 
	-> r2.d = r2.d;//r2.d==12 && r2.l==null && r2.r==null && 
	-> i2 = <TestInvoke: int a>;//$i2==11 && 
	-> r3.d = r3.d;//r3.d==11 && r3.l==null && r3.r==null && 
	-> i3 = <TestInvoke: int a>;//$i3==10 && 
	-> r4.d = r4.d;//r4.d==10 && r4.l==null && r4.r==null && 
	-> r1.l = r1.l;//r1.d==13 && r1.l==r2 && r1.r==null && 
	-> r2.l = r2.l;//r2.d==12 && r2.l==r3 && r2.r==null && 
	-> r3.l = r3.l;//r3.d==11 && r3.l==r4 && r3.r==null && 
	-> r5 = r1;//r5.d==13]r5.l==r2]r5.r==null]
	-> i9 = i9 + 1;//i9==34 && 
	-> i4 = r5.d;//$i4==13 && 
	-> r5 = r5.l;//r5.d==12]r5.l==r3]r5.r==null]
	-> i8 = i8 + -1;//i8==2 && 
	-> i9 = i9 + 1;//i9==35 && 
	-> i4 = r5.d;//$i4==12 && 
	-> r5 = r5.l;//r5.d==11]r5.l==r4]r5.r==null]
	-> i8 = i8 + -1;//i8==1 && 
	-> i9 = i9 + 1;//i9==36 && 
	-> i4 = r5.d;//$i4==11 && 
	-> r5 = r5.l;//r5.d==10]r5.l==null]r5.r==null]
	-> i8 = i8 + -1;//i8==0 && 
	-> i9 = i9 + 1;//i9==37 && 
	-> i4 = r5.d;//$i4==10 && 
	-> r5 = r5.l;//
	-> i8 = i8 + -1;//i8==-1 && 
	}
	example {[i8==3]
	-> i9 = 33;//r0.d==0 && r0.l==null && r0.r==null && r1.d==2 && r1.l==null && r1.r==null && r2.d==3 && r2.l==null && r2.r==null && r3.d==4 && r3.l==null && r3.r==null && r4.d==5 && r4.l==null && r4.r==null && $i0==0 && $i1==0 && $i2==0 && $i3==0 && $i4==0 && $i5==0 && $i6==0 && $i7==0 && i8==3 && i9==33 && r5==null]
	-> i0 = <TestInvoke: int a>;//$i0==13 && 
	-> r1.d = r1.d;//r1.d==13 && r1.l==null && r1.r==null && 
	-> i1 = <TestInvoke: int a>;//$i1==12 && 
	-> r2.d = r2.d;//r2.d==12 && r2.l==null && r2.r==null && 
	-> i2 = <TestInvoke: int a>;//$i2==11 && 
	-> r3.d = r3.d;//r3.d==11 && r3.l==null && r3.r==null && 
	-> i3 = <TestInvoke: int a>;//$i3==10 && 
	-> r4.d = r4.d;//r4.d==10 && r4.l==null && r4.r==null && 
	-> r1.l = r1.l;//r1.d==13 && r1.l==r2 && r1.r==null && 
	-> r2.l = r2.l;//r2.d==12 && r2.l==r3 && r2.r==null && 
	-> r3.l = r3.l;//r3.d==11 && r3.l==r4 && r3.r==null && 
	-> r5 = r1;//r5.d==13]r5.l==r2]r5.r==null]
	-> i9 = i9 + 1;//i9==34 && 
	-> i4 = r5.d;//$i4==13 && 
	-> r5 = r5.l;//r5.d==12]r5.l==r3]r5.r==null]
	-> i8 = i8 + -1;//i8==2 && 
	-> i9 = i9 + 1;//i9==35 && 
	-> i4 = r5.d;//$i4==12 && 
	-> r5 = r5.l;//r5.d==11]r5.l==r4]r5.r==null]
	-> i8 = i8 + -1;//i8==1 && 
	-> i9 = i9 + 1;//i9==36 && 
	-> i4 = r5.d;//$i4==11 && 
	-> r5 = r5.l;//r5.d==10]r5.l==null]r5.r==null]
	-> i8 = i8 + -1;//i8==0 && 
	-> i9 = i9 + 1;//i9==37 && 
	-> i4 = r5.d;//$i4==10 && 
	-> r5 = r5.l;//
	-> i8 = i8 + -1;//i8==-1 && 
	}
	example {[
	-> i9 = 33;//r0.d==0 && r0.l==null && r0.r==null && r1.d==2 && r1.l==null && r1.r==null && r2.d==3 && r2.l==null && r2.r==null && r3.d==4 && r3.l==null && r3.r==null && r4.d==5 && r4.l==null && r4.r==null && $i0==0 && $i1==0 && $i2==0 && $i3==0 && $i4==0 && $i5==0 && $i6==0 && $i7==0 && i8==3 && i9==33 && r5==null]
	-> i0 = <TestInvoke: int a>;//$i0==13 && 
	-> r1.d = r1.d;//r1.d==13 && r1.l==null && r1.r==null && 
	-> i1 = <TestInvoke: int a>;//$i1==12 && 
	-> r2.d = r2.d;//r2.d==12 && r2.l==null && r2.r==null && 
	-> i2 = <TestInvoke: int a>;//$i2==11 && 
	-> r3.d = r3.d;//r3.d==11 && r3.l==null && r3.r==null && 
	-> i3 = <TestInvoke: int a>;//$i3==10 && 
	-> r4.d = r4.d;//r4.d==10 && r4.l==null && r4.r==null && 
	-> r1.l = r1.l;//r1.d==13 && r1.l==r2 && r1.r==null && 
	-> r2.l = r2.l;//r2.d==12 && r2.l==r3 && r2.r==null && 
	-> r3.l = r3.l;//r3.d==11 && r3.l==r4 && r3.r==null && 
	-> r5 = r1;//r5.d==13]r5.l==r2]r5.r==null]
	-> i9 = i9 + 1;//i9==34 && 
	-> i4 = r5.d;//$i4==13 && 
	-> r5 = r5.l;//r5.d==12]r5.l==r3]r5.r==null]
	-> i8 = i8 + -1;//i8==2 && 
	-> i9 = i9 + 1;//i9==35 && 
	-> i4 = r5.d;//$i4==12 && 
	-> r5 = r5.l;//r5.d==11]r5.l==r4]r5.r==null]
	-> i8 = i8 + -1;//i8==1 && 
	-> i9 = i9 + 1;//i9==36 && 
	-> i4 = r5.d;//$i4==11 && 
	-> r5 = r5.l;//r5.d==10]r5.l==null]r5.r==null]
	-> i8 = i8 + -1;//i8==0 && 
	-> i9 = i9 + 1;//i9==37 && 
	-> i4 = r5.d;//$i4==10 && 
	-> r5 = r5.l;//
	-> i8 = i8 + -1;//i8==-1 && 
	}
	example {[i8==3]
	-> i9 = 33;//r0.d==0 && r0.l==null && r0.r==null && r1.d==2 && r1.l==null && r1.r==null && r2.d==3 && r2.l==null && r2.r==null && r3.d==4 && r3.l==null && r3.r==null && r4.d==5 && r4.l==null && r4.r==null && $i0==0 && $i1==0 && $i2==0 && $i3==0 && $i4==0 && $i5==0 && $i6==0 && $i7==0 && i8==3 && i9==33 && r5==null]
	-> i0 = <TestInvoke: int a>;//$i0==13 && 
	-> r1.d = r1.d;//r1.d==13 && r1.l==null && r1.r==null && 
	-> i1 = <TestInvoke: int a>;//$i1==12 && 
	-> r2.d = r2.d;//r2.d==12 && r2.l==null && r2.r==null && 
	-> i2 = <TestInvoke: int a>;//$i2==11 && 
	-> r3.d = r3.d;//r3.d==11 && r3.l==null && r3.r==null && 
	-> i3 = <TestInvoke: int a>;//$i3==10 && 
	-> r4.d = r4.d;//r4.d==10 && r4.l==null && r4.r==null && 
	-> r1.l = r1.l;//r1.d==13 && r1.l==r2 && r1.r==null && 
	-> r2.l = r2.l;//r2.d==12 && r2.l==r3 && r2.r==null && 
	-> r3.l = r3.l;//r3.d==11 && r3.l==r4 && r3.r==null && 
	-> r5 = r1;//r5.d==13]r5.l==r2]r5.r==null]
	-> i9 = i9 + 1;//i9==34 && 
	-> i4 = r5.d;//$i4==13 && 
	-> r5 = r5.l;//r5.d==12]r5.l==r3]r5.r==null]
	-> i8 = i8 + -1;//i8==2 && 
	-> i9 = i9 + 1;//i9==35 && 
	-> i4 = r5.d;//$i4==12 && 
	-> r5 = r5.l;//r5.d==11]r5.l==r4]r5.r==null]
	-> i8 = i8 + -1;//i8==1 && 
	-> i9 = i9 + 1;//i9==36 && 
	-> i4 = r5.d;//$i4==11 && 
	-> r5 = r5.l;//r5.d==10]r5.l==null]r5.r==null]
	-> i8 = i8 + -1;//i8==0 && 
	-> i9 = i9 + 1;//i9==37 && 
	-> i4 = r5.d;//$i4==10 && 
	-> r5 = r5.l;//
	-> i8 = i8 + -1;//i8==-1 && 
	}
	example {[
	-> i9 = 33;//r0.d==0 && r0.l==null && r0.r==null && r1.d==2 && r1.l==null && r1.r==null && r2.d==3 && r2.l==null && r2.r==null && r3.d==4 && r3.l==null && r3.r==null && r4.d==5 && r4.l==null && r4.r==null && $i0==0 && $i1==0 && $i2==0 && $i3==0 && $i4==0 && $i5==0 && $i6==0 && $i7==0 && i8==3 && i9==33 && r5==null]
	-> i0 = <TestInvoke: int a>;//$i0==13 && 
	-> r1.d = r1.d;//r1.d==13 && r1.l==null && r1.r==null && 
	-> i1 = <TestInvoke: int a>;//$i1==12 && 
	-> r2.d = r2.d;//r2.d==12 && r2.l==null && r2.r==null && 
	-> i2 = <TestInvoke: int a>;//$i2==11 && 
	-> r3.d = r3.d;//r3.d==11 && r3.l==null && r3.r==null && 
	-> i3 = <TestInvoke: int a>;//$i3==10 && 
	-> r4.d = r4.d;//r4.d==10 && r4.l==null && r4.r==null && 
	-> r1.l = r1.l;//r1.d==13 && r1.l==r2 && r1.r==null && 
	-> r2.l = r2.l;//r2.d==12 && r2.l==r3 && r2.r==null && 
	-> r3.l = r3.l;//r3.d==11 && r3.l==r4 && r3.r==null && 
	-> r5 = r1;//r5.d==13]r5.l==r2]r5.r==null]
	-> i9 = i9 + 1;//i9==34 && 
	-> i4 = r5.d;//$i4==13 && 
	-> r5 = r5.l;//r5.d==12]r5.l==r3]r5.r==null]
	-> i8 = i8 + -1;//i8==2 && 
	-> i9 = i9 + 1;//i9==35 && 
	-> i4 = r5.d;//$i4==12 && 
	-> r5 = r5.l;//r5.d==11]r5.l==r4]r5.r==null]
	-> i8 = i8 + -1;//i8==1 && 
	-> i9 = i9 + 1;//i9==36 && 
	-> i4 = r5.d;//$i4==11 && 
	-> r5 = r5.l;//r5.d==10]r5.l==null]r5.r==null]
	-> i8 = i8 + -1;//i8==0 && 
	-> i9 = i9 + 1;//i9==37 && 
	-> i4 = r5.d;//$i4==10 && 
	-> r5 = r5.l;//
	-> i8 = i8 + -1;//i8==-1 && 
	}
	example {[i8==3]
	-> i9 = 33;//r0.d==0 && r0.l==null && r0.r==null && r1.d==2 && r1.l==null && r1.r==null && r2.d==3 && r2.l==null && r2.r==null && r3.d==4 && r3.l==null && r3.r==null && r4.d==5 && r4.l==null && r4.r==null && $i0==0 && $i1==0 && $i2==0 && $i3==0 && $i4==0 && $i5==0 && $i6==0 && $i7==0 && i8==3 && i9==33 && r5==null]
	-> i0 = <TestInvoke: int a>;//$i0==13 && 
	-> r1.d = r1.d;//r1.d==13 && r1.l==null && r1.r==null && 
	-> i1 = <TestInvoke: int a>;//$i1==12 && 
	-> r2.d = r2.d;//r2.d==12 && r2.l==null && r2.r==null && 
	-> i2 = <TestInvoke: int a>;//$i2==11 && 
	-> r3.d = r3.d;//r3.d==11 && r3.l==null && r3.r==null && 
	-> i3 = <TestInvoke: int a>;//$i3==10 && 
	-> r4.d = r4.d;//r4.d==10 && r4.l==null && r4.r==null && 
	-> r1.l = r1.l;//r1.d==13 && r1.l==r2 && r1.r==null && 
	-> r2.l = r2.l;//r2.d==12 && r2.l==r3 && r2.r==null && 
	-> r3.l = r3.l;//r3.d==11 && r3.l==r4 && r3.r==null && 
	-> r5 = r1;//r5.d==13]r5.l==r2]r5.r==null]
	-> i9 = i9 + 1;//i9==34 && 
	-> i4 = r5.d;//$i4==13 && 
	-> r5 = r5.l;//r5.d==12]r5.l==r3]r5.r==null]
	-> i8 = i8 + -1;//i8==2 && 
	-> i9 = i9 + 1;//i9==35 && 
	-> i4 = r5.d;//$i4==12 && 
	-> r5 = r5.l;//r5.d==11]r5.l==r4]r5.r==null]
	-> i8 = i8 + -1;//i8==1 && 
	-> i9 = i9 + 1;//i9==36 && 
	-> i4 = r5.d;//$i4==11 && 
	-> r5 = r5.l;//r5.d==10]r5.l==null]r5.r==null]
	-> i8 = i8 + -1;//i8==0 && 
	-> i9 = i9 + 1;//i9==37 && 
	-> i4 = r5.d;//$i4==10 && 
	-> r5 = r5.l;//
	-> i8 = i8 + -1;//i8==-1 && 
	}
	example {[
	-> i9 = 33;//r0.d==0 && r0.l==null && r0.r==null && r1.d==2 && r1.l==null && r1.r==null && r2.d==3 && r2.l==null && r2.r==null && r3.d==4 && r3.l==null && r3.r==null && r4.d==5 && r4.l==null && r4.r==null && $i0==0 && $i1==0 && $i2==0 && $i3==0 && $i4==0 && $i5==0 && $i6==0 && $i7==0 && i8==3 && i9==33 && r5==null]
	-> i0 = <TestInvoke: int a>;//$i0==13 && 
	-> r1.d = r1.d;//r1.d==13 && r1.l==null && r1.r==null && 
	-> i1 = <TestInvoke: int a>;//$i1==12 && 
	-> r2.d = r2.d;//r2.d==12 && r2.l==null && r2.r==null && 
	-> i2 = <TestInvoke: int a>;//$i2==11 && 
	-> r3.d = r3.d;//r3.d==11 && r3.l==null && r3.r==null && 
	-> i3 = <TestInvoke: int a>;//$i3==10 && 
	-> r4.d = r4.d;//r4.d==10 && r4.l==null && r4.r==null && 
	-> r1.l = r1.l;//r1.d==13 && r1.l==r2 && r1.r==null && 
	-> r2.l = r2.l;//r2.d==12 && r2.l==r3 && r2.r==null && 
	-> r3.l = r3.l;//r3.d==11 && r3.l==r4 && r3.r==null && 
	-> r5 = r1;//r5.d==13]r5.l==r2]r5.r==null]
	-> i9 = i9 + 1;//i9==34 && 
	-> i4 = r5.d;//$i4==13 && 
	-> r5 = r5.l;//r5.d==12]r5.l==r3]r5.r==null]
	-> i8 = i8 + -1;//i8==2 && 
	-> i9 = i9 + 1;//i9==35 && 
	-> i4 = r5.d;//$i4==12 && 
	-> r5 = r5.l;//r5.d==11]r5.l==r4]r5.r==null]
	-> i8 = i8 + -1;//i8==1 && 
	-> i9 = i9 + 1;//i9==36 && 
	-> i4 = r5.d;//$i4==11 && 
	-> r5 = r5.l;//r5.d==10]r5.l==null]r5.r==null]
	-> i8 = i8 + -1;//i8==0 && 
	-> i9 = i9 + 1;//i9==37 && 
	-> i4 = r5.d;//$i4==10 && 
	-> r5 = r5.l;//
	-> i8 = i8 + -1;//i8==-1 && 
	}
	example {[i8==3]
	-> i9 = 33;//r0.d==0 && r0.l==null && r0.r==null && r1.d==2 && r1.l==null && r1.r==null && r2.d==3 && r2.l==null && r2.r==null && r3.d==4 && r3.l==null && r3.r==null && r4.d==5 && r4.l==null && r4.r==null && $i0==0 && $i1==0 && $i2==0 && $i3==0 && $i4==0 && $i5==0 && $i6==0 && $i7==0 && i8==3 && i9==33 && r5==null]
	-> i0 = <TestInvoke: int a>;//$i0==13 && 
	-> r1.d = r1.d;//r1.d==13 && r1.l==null && r1.r==null && 
	-> i1 = <TestInvoke: int a>;//$i1==12 && 
	-> r2.d = r2.d;//r2.d==12 && r2.l==null && r2.r==null && 
	-> i2 = <TestInvoke: int a>;//$i2==11 && 
	-> r3.d = r3.d;//r3.d==11 && r3.l==null && r3.r==null && 
	-> i3 = <TestInvoke: int a>;//$i3==10 && 
	-> r4.d = r4.d;//r4.d==10 && r4.l==null && r4.r==null && 
	-> r1.l = r1.l;//r1.d==13 && r1.l==r2 && r1.r==null && 
	-> r2.l = r2.l;//r2.d==12 && r2.l==r3 && r2.r==null && 
	-> r3.l = r3.l;//r3.d==11 && r3.l==r4 && r3.r==null && 
	-> r5 = r1;//r5.d==13]r5.l==r2]r5.r==null]
	-> i9 = i9 + 1;//i9==34 && 
	-> i4 = r5.d;//$i4==13 && 
	-> r5 = r5.l;//r5.d==12]r5.l==r3]r5.r==null]
	-> i8 = i8 + -1;//i8==2 && 
	-> i9 = i9 + 1;//i9==35 && 
	-> i4 = r5.d;//$i4==12 && 
	-> r5 = r5.l;//r5.d==11]r5.l==r4]r5.r==null]
	-> i8 = i8 + -1;//i8==1 && 
	-> i9 = i9 + 1;//i9==36 && 
	-> i4 = r5.d;//$i4==11 && 
	-> r5 = r5.l;//r5.d==10]r5.l==null]r5.r==null]
	-> i8 = i8 + -1;//i8==0 && 
	-> i9 = i9 + 1;//i9==37 && 
	-> i4 = r5.d;//$i4==10 && 
	-> r5 = r5.l;//
	-> i8 = i8 + -1;//i8==-1 && 
	}

}
