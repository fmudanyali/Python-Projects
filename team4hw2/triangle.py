#!/usr/local/bin/python3
import sys
import stdio
num1 = int(sys.argv[1])
num2 = int(sys.argv[2])
num3 = int(sys.argv[3])
if num1 <= num2+num3 and num2 <= num1+num3 and num3 <= num1+num2:
    stdio.writeln("True")
else:
    stdio.writeln("False")
