import sys
import stdio
a = int(sys.argv[1])
b = int(sys.argv[2])
c = int(sys.argv[3])
if a <= b+c and b <= a+c and c <= a+b:
    stdio.writeln("True")
else:
    stdio.writeln("False")
