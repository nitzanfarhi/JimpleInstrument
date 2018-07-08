goo (mut i0:int,mut i1:int) -> (res:int){
	example {[i0==1 && i1==3]
	-> i1 = i1 - i0;//
	-> i1 = i1 - i0;//
	}
	example {[i0==2 && i1==3]
	-> i1 = i1 - i0;//
	-> i0 = i0 - i1;//
	}
	example {[i0==3 && i1==3]
	-> i0 = i0 - i1;//
	-> i0 = i0 - i1;//
	-> i0 = i0 - i1;//
	-> i0 = i0 - i1;//
	-> i0 = i0 - i1;//
	-> i0 = i0 - i1;//
	-> i0 = i0 - i1;//
	-> i0 = i0 - i1;//
	-> i0 = i0 - i1;//
	}
	example {[i0==4 && i1==3]
	-> i0 = i0 - i1;//
	-> i1 = i1 - i0;//
	-> i1 = i1 - i0;//
	}
	example {[i0==5 && i1==3]
	-> i0 = i0 - i1;//
	-> i1 = i1 - i0;//
	-> i0 = i0 - i1;//
	}
	example {[i0==6 && i1==3]
	-> i0 = i0 - i1;//
	}
	example {[i0==7 && i1==3]
	}
	example {[i0==8 && i1==3]
	-> i0 = i0 - i1;//
	-> i0 = i0 - i1;//
	-> i1 = i1 - i0;//
	-> i0 = i0 - i1;//
	}
	example {[i0==9 && i1==3]
	-> i0 = i0 - i1;//
	-> i0 = i0 - i1;//
	}
	example {[i0==10 && i1==3]
	-> i0 = i0 - i1;//
	-> i0 = i0 - i1;//
	-> i0 = i0 - i1;//
	-> i1 = i1 - i0;//
	-> i1 = i1 - i0;//
	}
	example {[i0==11 && i1==3]
	-> i0 = i0 - i1;//
	-> i0 = i0 - i1;//
	-> i0 = i0 - i1;//
	-> i1 = i1 - i0;//
	-> i0 = i0 - i1;//
	}

}
