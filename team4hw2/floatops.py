#!/usr/local/bin/python3
#Furkan Mudanyalı 20181701088
#Emir Öztürk      20181701062
import stdio,sys

a,b=float(sys.argv[1]),float(sys.argv[2])
total,diff,prod,quot,rem,exp=a+b,a-b,a*b,a//b,a%b,a**b
stdio.writeln(str(a)+" + "+str(b)+" = "+str(total))
stdio.writeln(str(a)+" - "+str(b)+" = "+str(diff))
stdio.writeln(str(a)+" * "+str(b)+" = "+str(prod))
stdio.writeln(str(a)+" // "+str(b)+" = "+str(quot))
stdio.writeln(str(a)+" % "+str(b)+" = "+str(rem))
stdio.writeln(str(a)+" ** "+str(b)+" = "+str(exp))
