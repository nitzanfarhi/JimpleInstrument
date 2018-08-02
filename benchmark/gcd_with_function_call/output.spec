gcd (mut i0:int,mut i1:int) -> (res:int){

	example {[i0==125 && i1==34]
	-> i0 = getA(i0, i1);//i0==91 && 
	-> i0 = getA(i0, i1);//i0==57 && 
	-> i0 = getA(i0, i1);//i0==23 && 
	-> i1 = getB(i0, i1);//i1==11]
	-> i0 = getA(i0, i1);//i0==12 && 
	-> i0 = getA(i0, i1);//i0==1 && 
	-> i1 = getB(i0, i1);//i1==10]
	-> i1 = getB(i0, i1);//i1==9]
	-> i1 = getB(i0, i1);//i1==8]
	-> i1 = getB(i0, i1);//i1==7]
	-> i1 = getB(i0, i1);//i1==6]
	-> i1 = getB(i0, i1);//i1==5]
	-> i1 = getB(i0, i1);//i1==4]
	-> i1 = getB(i0, i1);//i1==3]
	-> i1 = getB(i0, i1);//i1==2]
	-> i1 = getB(i0, i1);//i1==1]
	}
	example {[i0==126 && i1==35]
	-> i0 = getA(i0, i1);//i0==91 && 
	-> i0 = getA(i0, i1);//i0==56 && 
	-> i0 = getA(i0, i1);//i0==21 && 
	-> i1 = getB(i0, i1);//i1==14]
	-> i0 = getA(i0, i1);//i0==7 && 
	-> i1 = getB(i0, i1);//i1==7]
	}
	example {[i0==127 && i1==36]
	-> i0 = getA(i0, i1);//i0==91 && 
	-> i0 = getA(i0, i1);//i0==55 && 
	-> i0 = getA(i0, i1);//i0==19 && 
	-> i1 = getB(i0, i1);//i1==17]
	-> i0 = getA(i0, i1);//i0==2 && 
	-> i1 = getB(i0, i1);//i1==15]
	-> i1 = getB(i0, i1);//i1==13]
	-> i1 = getB(i0, i1);//i1==11]
	-> i1 = getB(i0, i1);//i1==9]
	-> i1 = getB(i0, i1);//i1==7]
	-> i1 = getB(i0, i1);//i1==5]
	-> i1 = getB(i0, i1);//i1==3]
	-> i1 = getB(i0, i1);//i1==1]
	-> i0 = getA(i0, i1);//i0==1 && 
	}
	example {[i0==128 && i1==37]
	-> i0 = getA(i0, i1);//i0==91 && 
	-> i0 = getA(i0, i1);//i0==54 && 
	-> i0 = getA(i0, i1);//i0==17 && 
	-> i1 = getB(i0, i1);//i1==20]
	-> i1 = getB(i0, i1);//i1==3]
	-> i0 = getA(i0, i1);//i0==14 && 
	-> i0 = getA(i0, i1);//i0==11 && 
	-> i0 = getA(i0, i1);//i0==8 && 
	-> i0 = getA(i0, i1);//i0==5 && 
	-> i0 = getA(i0, i1);//i0==2 && 
	-> i1 = getB(i0, i1);//i1==1]
	-> i0 = getA(i0, i1);//i0==1 && 
	}
	example {[i0==129 && i1==38]
	-> i0 = getA(i0, i1);//i0==91 && 
	-> i0 = getA(i0, i1);//i0==53 && 
	-> i0 = getA(i0, i1);//i0==15 && 
	-> i1 = getB(i0, i1);//i1==23]
	-> i1 = getB(i0, i1);//i1==8]
	-> i0 = getA(i0, i1);//i0==7 && 
	-> i1 = getB(i0, i1);//i1==1]
	-> i0 = getA(i0, i1);//i0==6 && 
	-> i0 = getA(i0, i1);//i0==5 && 
	-> i0 = getA(i0, i1);//i0==4 && 
	-> i0 = getA(i0, i1);//i0==3 && 
	-> i0 = getA(i0, i1);//i0==2 && 
	-> i0 = getA(i0, i1);//i0==1 && 
	}
	example {[i0==130 && i1==39]
	-> i0 = getA(i0, i1);//i0==91 && 
	-> i0 = getA(i0, i1);//i0==52 && 
	-> i0 = getA(i0, i1);//i0==13 && 
	-> i1 = getB(i0, i1);//i1==26]
	-> i1 = getB(i0, i1);//i1==13]
	}
	example {[i0==131 && i1==40]
	-> i0 = getA(i0, i1);//i0==91 && 
	-> i0 = getA(i0, i1);//i0==51 && 
	-> i0 = getA(i0, i1);//i0==11 && 
	-> i1 = getB(i0, i1);//i1==29]
	-> i1 = getB(i0, i1);//i1==18]
	-> i1 = getB(i0, i1);//i1==7]
	-> i0 = getA(i0, i1);//i0==4 && 
	-> i1 = getB(i0, i1);//i1==3]
	-> i0 = getA(i0, i1);//i0==1 && 
	-> i1 = getB(i0, i1);//i1==2]
	-> i1 = getB(i0, i1);//i1==1]
	}
	example {[i0==132 && i1==41]
	-> i0 = getA(i0, i1);//i0==91 && 
	-> i0 = getA(i0, i1);//i0==50 && 
	-> i0 = getA(i0, i1);//i0==9 && 
	-> i1 = getB(i0, i1);//i1==32]
	-> i1 = getB(i0, i1);//i1==23]
	-> i1 = getB(i0, i1);//i1==14]
	-> i1 = getB(i0, i1);//i1==5]
	-> i0 = getA(i0, i1);//i0==4 && 
	-> i1 = getB(i0, i1);//i1==1]
	-> i0 = getA(i0, i1);//i0==3 && 
	-> i0 = getA(i0, i1);//i0==2 && 
	-> i0 = getA(i0, i1);//i0==1 && 
	}
	example {[i0==133 && i1==42]
	-> i0 = getA(i0, i1);//i0==91 && 
	-> i0 = getA(i0, i1);//i0==49 && 
	-> i0 = getA(i0, i1);//i0==7 && 
	-> i1 = getB(i0, i1);//i1==35]
	-> i1 = getB(i0, i1);//i1==28]
	-> i1 = getB(i0, i1);//i1==21]
	-> i1 = getB(i0, i1);//i1==14]
	-> i1 = getB(i0, i1);//i1==7]
	}
	example {[i0==134 && i1==43]
	-> i0 = getA(i0, i1);//i0==91 && 
	-> i0 = getA(i0, i1);//i0==48 && 
	-> i0 = getA(i0, i1);//i0==5 && 
	-> i1 = getB(i0, i1);//i1==38]
	-> i1 = getB(i0, i1);//i1==33]
	-> i1 = getB(i0, i1);//i1==28]
	-> i1 = getB(i0, i1);//i1==23]
	-> i1 = getB(i0, i1);//i1==18]
	-> i1 = getB(i0, i1);//i1==13]
	-> i1 = getB(i0, i1);//i1==8]
	-> i1 = getB(i0, i1);//i1==3]
	-> i0 = getA(i0, i1);//i0==2 && 
	-> i1 = getB(i0, i1);//i1==1]
	-> i0 = getA(i0, i1);//i0==1 && 
	}
	example {[i0==135 && i1==44]
	-> i0 = getA(i0, i1);//i0==91 && 
	-> i0 = getA(i0, i1);//i0==47 && 
	-> i0 = getA(i0, i1);//i0==3 && 
	-> i1 = getB(i0, i1);//i1==41]
	-> i1 = getB(i0, i1);//i1==38]
	-> i1 = getB(i0, i1);//i1==35]
	-> i1 = getB(i0, i1);//i1==32]
	-> i1 = getB(i0, i1);//i1==29]
	-> i1 = getB(i0, i1);//i1==26]
	-> i1 = getB(i0, i1);//i1==23]
	-> i1 = getB(i0, i1);//i1==20]
	-> i1 = getB(i0, i1);//i1==17]
	-> i1 = getB(i0, i1);//i1==14]
	-> i1 = getB(i0, i1);//i1==11]
	-> i1 = getB(i0, i1);//i1==8]
	-> i1 = getB(i0, i1);//i1==5]
	-> i1 = getB(i0, i1);//i1==2]
	-> i0 = getA(i0, i1);//i0==1 && 
	-> i1 = getB(i0, i1);//i1==1]
	}
	example {[i0==136 && i1==45]
	-> i0 = getA(i0, i1);//i0==91 && 
	-> i0 = getA(i0, i1);//i0==46 && 
	-> i0 = getA(i0, i1);//i0==1 && 
	-> i1 = getB(i0, i1);//i1==44]
	-> i1 = getB(i0, i1);//i1==43]
	-> i1 = getB(i0, i1);//i1==42]
	-> i1 = getB(i0, i1);//i1==41]
	-> i1 = getB(i0, i1);//i1==40]
	-> i1 = getB(i0, i1);//i1==39]
	-> i1 = getB(i0, i1);//i1==38]
	-> i1 = getB(i0, i1);//i1==37]
	-> i1 = getB(i0, i1);//i1==36]
	-> i1 = getB(i0, i1);//i1==35]
	-> i1 = getB(i0, i1);//i1==34]
	-> i1 = getB(i0, i1);//i1==33]
	-> i1 = getB(i0, i1);//i1==32]
	-> i1 = getB(i0, i1);//i1==31]
	-> i1 = getB(i0, i1);//i1==30]
	-> i1 = getB(i0, i1);//i1==29]
	-> i1 = getB(i0, i1);//i1==28]
	-> i1 = getB(i0, i1);//i1==27]
	-> i1 = getB(i0, i1);//i1==26]
	-> i1 = getB(i0, i1);//i1==25]
	-> i1 = getB(i0, i1);//i1==24]
	-> i1 = getB(i0, i1);//i1==23]
	-> i1 = getB(i0, i1);//i1==22]
	-> i1 = getB(i0, i1);//i1==21]
	-> i1 = getB(i0, i1);//i1==20]
	-> i1 = getB(i0, i1);//i1==19]
	-> i1 = getB(i0, i1);//i1==18]
	-> i1 = getB(i0, i1);//i1==17]
	-> i1 = getB(i0, i1);//i1==16]
	-> i1 = getB(i0, i1);//i1==15]
	-> i1 = getB(i0, i1);//i1==14]
	-> i1 = getB(i0, i1);//i1==13]
	-> i1 = getB(i0, i1);//i1==12]
	-> i1 = getB(i0, i1);//i1==11]
	-> i1 = getB(i0, i1);//i1==10]
	-> i1 = getB(i0, i1);//i1==9]
	-> i1 = getB(i0, i1);//i1==8]
	-> i1 = getB(i0, i1);//i1==7]
	-> i1 = getB(i0, i1);//i1==6]
	-> i1 = getB(i0, i1);//i1==5]
	-> i1 = getB(i0, i1);//i1==4]
	-> i1 = getB(i0, i1);//i1==3]
	-> i1 = getB(i0, i1);//i1==2]
	-> i1 = getB(i0, i1);//i1==1]
	}
	example {[i0==137 && i1==46]
	-> i0 = getA(i0, i1);//i0==91 && 
	-> i0 = getA(i0, i1);//i0==45 && 
	-> i1 = getB(i0, i1);//i1==1]
	-> i0 = getA(i0, i1);//i0==44 && 
	-> i0 = getA(i0, i1);//i0==43 && 
	-> i0 = getA(i0, i1);//i0==42 && 
	-> i0 = getA(i0, i1);//i0==41 && 
	-> i0 = getA(i0, i1);//i0==40 && 
	-> i0 = getA(i0, i1);//i0==39 && 
	-> i0 = getA(i0, i1);//i0==38 && 
	-> i0 = getA(i0, i1);//i0==37 && 
	-> i0 = getA(i0, i1);//i0==36 && 
	-> i0 = getA(i0, i1);//i0==35 && 
	-> i0 = getA(i0, i1);//i0==34 && 
	-> i0 = getA(i0, i1);//i0==33 && 
	-> i0 = getA(i0, i1);//i0==32 && 
	-> i0 = getA(i0, i1);//i0==31 && 
	-> i0 = getA(i0, i1);//i0==30 && 
	-> i0 = getA(i0, i1);//i0==29 && 
	-> i0 = getA(i0, i1);//i0==28 && 
	-> i0 = getA(i0, i1);//i0==27 && 
	-> i0 = getA(i0, i1);//i0==26 && 
	-> i0 = getA(i0, i1);//i0==25 && 
	-> i0 = getA(i0, i1);//i0==24 && 
	-> i0 = getA(i0, i1);//i0==23 && 
	-> i0 = getA(i0, i1);//i0==22 && 
	-> i0 = getA(i0, i1);//i0==21 && 
	-> i0 = getA(i0, i1);//i0==20 && 
	-> i0 = getA(i0, i1);//i0==19 && 
	-> i0 = getA(i0, i1);//i0==18 && 
	-> i0 = getA(i0, i1);//i0==17 && 
	-> i0 = getA(i0, i1);//i0==16 && 
	-> i0 = getA(i0, i1);//i0==15 && 
	-> i0 = getA(i0, i1);//i0==14 && 
	-> i0 = getA(i0, i1);//i0==13 && 
	-> i0 = getA(i0, i1);//i0==12 && 
	-> i0 = getA(i0, i1);//i0==11 && 
	-> i0 = getA(i0, i1);//i0==10 && 
	-> i0 = getA(i0, i1);//i0==9 && 
	-> i0 = getA(i0, i1);//i0==8 && 
	-> i0 = getA(i0, i1);//i0==7 && 
	-> i0 = getA(i0, i1);//i0==6 && 
	-> i0 = getA(i0, i1);//i0==5 && 
	-> i0 = getA(i0, i1);//i0==4 && 
	-> i0 = getA(i0, i1);//i0==3 && 
	-> i0 = getA(i0, i1);//i0==2 && 
	-> i0 = getA(i0, i1);//i0==1 && 
	}
	example {[i0==138 && i1==47]
	-> i0 = getA(i0, i1);//i0==91 && 
	-> i0 = getA(i0, i1);//i0==44 && 
	-> i1 = getB(i0, i1);//i1==3]
	-> i0 = getA(i0, i1);//i0==41 && 
	-> i0 = getA(i0, i1);//i0==38 && 
	-> i0 = getA(i0, i1);//i0==35 && 
	-> i0 = getA(i0, i1);//i0==32 && 
	-> i0 = getA(i0, i1);//i0==29 && 
	-> i0 = getA(i0, i1);//i0==26 && 
	-> i0 = getA(i0, i1);//i0==23 && 
	-> i0 = getA(i0, i1);//i0==20 && 
	-> i0 = getA(i0, i1);//i0==17 && 
	-> i0 = getA(i0, i1);//i0==14 && 
	-> i0 = getA(i0, i1);//i0==11 && 
	-> i0 = getA(i0, i1);//i0==8 && 
	-> i0 = getA(i0, i1);//i0==5 && 
	-> i0 = getA(i0, i1);//i0==2 && 
	-> i1 = getB(i0, i1);//i1==1]
	-> i0 = getA(i0, i1);//i0==1 && 
	}
	example {[i0==139 && i1==48]
	-> i0 = getA(i0, i1);//i0==91 && 
	-> i0 = getA(i0, i1);//i0==43 && 
	-> i1 = getB(i0, i1);//i1==5]
	-> i0 = getA(i0, i1);//i0==38 && 
	-> i0 = getA(i0, i1);//i0==33 && 
	-> i0 = getA(i0, i1);//i0==28 && 
	-> i0 = getA(i0, i1);//i0==23 && 
	-> i0 = getA(i0, i1);//i0==18 && 
	-> i0 = getA(i0, i1);//i0==13 && 
	-> i0 = getA(i0, i1);//i0==8 && 
	-> i0 = getA(i0, i1);//i0==3 && 
	-> i1 = getB(i0, i1);//i1==2]
	-> i0 = getA(i0, i1);//i0==1 && 
	-> i1 = getB(i0, i1);//i1==1]
	}
	example {[i0==140 && i1==49]
	-> i0 = getA(i0, i1);//i0==91 && 
	-> i0 = getA(i0, i1);//i0==42 && 
	-> i1 = getB(i0, i1);//i1==7]
	-> i0 = getA(i0, i1);//i0==35 && 
	-> i0 = getA(i0, i1);//i0==28 && 
	-> i0 = getA(i0, i1);//i0==21 && 
	-> i0 = getA(i0, i1);//i0==14 && 
	-> i0 = getA(i0, i1);//i0==7 && 
	}
	example {[i0==141 && i1==50]
	-> i0 = getA(i0, i1);//i0==91 && 
	-> i0 = getA(i0, i1);//i0==41 && 
	-> i1 = getB(i0, i1);//i1==9]
	-> i0 = getA(i0, i1);//i0==32 && 
	-> i0 = getA(i0, i1);//i0==23 && 
	-> i0 = getA(i0, i1);//i0==14 && 
	-> i0 = getA(i0, i1);//i0==5 && 
	-> i1 = getB(i0, i1);//i1==4]
	-> i0 = getA(i0, i1);//i0==1 && 
	-> i1 = getB(i0, i1);//i1==3]
	-> i1 = getB(i0, i1);//i1==2]
	-> i1 = getB(i0, i1);//i1==1]
	}
	example {[i0==142 && i1==51]
	-> i0 = getA(i0, i1);//i0==91 && 
	-> i0 = getA(i0, i1);//i0==40 && 
	-> i1 = getB(i0, i1);//i1==11]
	-> i0 = getA(i0, i1);//i0==29 && 
	-> i0 = getA(i0, i1);//i0==18 && 
	-> i0 = getA(i0, i1);//i0==7 && 
	-> i1 = getB(i0, i1);//i1==4]
	-> i0 = getA(i0, i1);//i0==3 && 
	-> i1 = getB(i0, i1);//i1==1]
	-> i0 = getA(i0, i1);//i0==2 && 
	-> i0 = getA(i0, i1);//i0==1 && 
	}
	example {[i0==143 && i1==52]
	-> i0 = getA(i0, i1);//i0==91 && 
	-> i0 = getA(i0, i1);//i0==39 && 
	-> i1 = getB(i0, i1);//i1==13]
	-> i0 = getA(i0, i1);//i0==26 && 
	-> i0 = getA(i0, i1);//i0==13 && 
	}
	example {[i0==144 && i1==53]
	-> i0 = getA(i0, i1);//i0==91 && 
	-> i0 = getA(i0, i1);//i0==38 && 
	-> i1 = getB(i0, i1);//i1==15]
	-> i0 = getA(i0, i1);//i0==23 && 
	-> i0 = getA(i0, i1);//i0==8 && 
	-> i1 = getB(i0, i1);//i1==7]
	-> i0 = getA(i0, i1);//i0==1 && 
	-> i1 = getB(i0, i1);//i1==6]
	-> i1 = getB(i0, i1);//i1==5]
	-> i1 = getB(i0, i1);//i1==4]
	-> i1 = getB(i0, i1);//i1==3]
	-> i1 = getB(i0, i1);//i1==2]
	-> i1 = getB(i0, i1);//i1==1]
	}

}
