#!/usr/local/bin/python3
#Emir Öztürk      20181701062
#Furkan Mudanyalı 20181701088
import sys,stdio
def checkerboard(x):
    for i in range(x):
        if i%2!=0: stdio.write(" ")
        for k in range(x):stdio.write("* ")
        stdio.writeln("")
if len(sys.argv)<2:stdio.writeln("Please give me an argument.")
elif not sys.argv[1].isdigit():stdio.writeln("Please give me a number.")
else: checkerboard(int(sys.argv[1]))
