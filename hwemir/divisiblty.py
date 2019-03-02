import sys,stdio

a = int(sys.argv[1])

if a%3 == 0 and a%2 == 0:
    stdio.writeln(str(a) + " is divisible by 6")
else:
    stdio.writeln(str(a) + " is not divisable by 6")
