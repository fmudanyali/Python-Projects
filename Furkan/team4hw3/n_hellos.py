#!/usr/local/bin/python3
#Emir Öztürk      20181701062
#Furkan Mudanyalı 20181701088
import sys,stdio
stdio.writeln("1st Hello")
stdio.writeln("2nd Hello")
stdio.writeln("3rd Hello")
i=4
while i<=int(sys.argv[1]):
    if i%100==0 and i<int(sys.argv[1]):
        stdio.writeln(str(i)+"th Hello")
        stdio.writeln(str(i+1)+"st Hello")
        stdio.writeln(str(i+2)+"nd Hello")
        stdio.writeln(str(i+3)+"rd Hello")
        i+=4
    elif i%10==0 and i<int(sys.argv[1]):
        stdio.writeln(str(i)+"th Hello")
        stdio.writeln(str(i+1)+"st Hello")
        stdio.writeln(str(i+2)+"nd Hello")
        stdio.writeln(str(i+3)+"rd Hello")
        i+=4
    stdio.writeln(str(i)+"th Hello")
    i+=1
