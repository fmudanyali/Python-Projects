import sys,stdio
if sys.argv[2] == "Celcius":
    C=float(sys.argv[1])
    F=(9/5*C)+32
    K=C+273.15
elif sys.argv[2] == "Fahreneit":
    F=float(sys.argv[1])
    C=(F-32)*5/9
    K=C+273.15
elif sys.argv[2]== "Kelvin":
    K=float(sys.argv[1])
    C=K-273.15
    F=(9/5*C)+32
else:
    stdio.writeln("Use celcius,Fahreneit or Kelvin")
    sys.exit()
stdio.writeln("Fahreneit " + str(F))
stdio.writeln("Celcius "+ str(C))
stdio.writeln("Kelvin "+ str(K))
