#!/usr/local/bin/python3
#Furkan MUDANYALI 20181701088
#Emir ÖZTÜRK 20181701062
import stdio,sys

def stats(numbers):
  array=[numbers[x] for x in range(1,len(numbers))]
  addition=0
  for i in range(len(array)): addition+=int(array[i])
  mean=addition/len(array)
  addition=0
  for i in range(len(array)): addition+=(int(array[i])-mean)**2
  var=addition/len(array)
  dev=var**0.5
  return mean,var,dev

#Failproofing
if len(sys.argv)<2:
  stdio.writeln("You must provide at least one argument.")
  sys.exit()
for i in range(1,len(sys.argv)):
  if not sys.argv[i].isdigit():
    stdio.writeln("All of your arguments must be numbers.")
    sys.exit()

mean,var,dev=stats(sys.argv)

stdio.writeln(mean)
stdio.writeln(var)
stdio.writeln(dev)