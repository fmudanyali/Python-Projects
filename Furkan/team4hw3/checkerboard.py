#!/usr/local/bin/python3
import sys,stdio
for i in range(int(sys.argv[1])):
    if i%2!=0: stdio.write(" ")
    for k in range(int(sys.argv[1])):
        stdio.write("* ")
    stdio.writeln("")
