#!/usr/local/bin/python3
#Emir Öztürk      20181701062
#Furkan Mudanyalı 20181701088
import stdio,sys
if not sys.argv[1].isdigit():
    stdio.writeln("Please give me a number.")
    sys.exit()
def temperature(x,y):
    if y == "Fahrenheit" or y == "fahrenheit" or y == "F":
        F=x
        C=(F-32)/1.8
        K=C+273.15
    elif y == "Celcius" or y == "celcius" or y == "C":
        C=x
        F=(9/5*C)+32
        K=C+273.15
    elif y == "Kelvin" or y == "kelvin" or y == "K":
        K=x
        C=K-273.15
        F=(9/5*C)+32
    else:
        stdio.writeln("Please give me Celcius, Fahrenheit or Kelvin.")
        sys.exit()
    stdio.writeln("Celcius = "+str(C))
    stdio.writeln("Fahrenheit = "+str(F))
    stdio.writeln("Kelvin = "+str(K))
if len(sys.argv)<3: stdio.writeln("Please give me 2 arguments.")
else: temperature(float(sys.argv[1]),sys.argv[2])
