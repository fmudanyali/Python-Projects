#!/usr/local/bin/python3
#Emir Öztürk      20181701062
#Furkan Mudanyalı 20181701088
import stdio,sys
if sys.argv[2] == "Fahrenheit":
    F=float(sys.argv[1])
    C=(F-32)/1.8
    K=C+273.15
elif sys.argv[2] == "Celcius":
    C=float(sys.argv[1])
    F=(9/5*C)+32
    K=C+273.15
elif sys.argv[2] == "Kelvin":
    K=float(sys.argv[1])
    C=K-273.15
    F=(9/5*C)+32
else:
    stdio.writeln("Please give me Celcius, Fahrenheit or Kelvin.")
    sys.exit()
stdio.writeln("Celcius = "+str(C))
stdio.writeln("Fahrenheit = "+str(F))
stdio.writeln("Kelvin = "+str(K))
