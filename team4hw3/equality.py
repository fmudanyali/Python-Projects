#!/usr/local/bin/python3
#Emir Öztürk      20181701062
#Furkan Mudanyalı 20181701088
import sys,stdio
def equality(x,y,z):
    if x==y==z:stdio.writeln("Equal")
    else:stdio.writeln("Not Equal")

if len(sys.argv)<4:stdio.writeln("Please give me at least 3 arguments.")
else: equality(int(sys.argv[1]),int(sys.argv[2]),int(sys.argv[3]))
