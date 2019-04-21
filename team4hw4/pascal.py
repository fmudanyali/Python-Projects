#!/usr/local/bin/python3
#Furkan MUDANYALI 20181701088
#Emir ÖZTÜRK 20181701062
import stdio,sys
def pascal(size):
  if size<0:
    stdio.writeln("Size cannot be smaller than 0.")
    sys.exit()
  a=[[1 for i in range(k+1)] for k in range(size+1)]
  for i in range(size+1):
    for k in range(1,i):
      a[i][k]=a[i-1][k-1]+a[i-1][k]
  return a

#Failproofing.
if len(sys.argv)<2:
  stdio.writeln("You must provide an argument.")
  sys.exit()
elif not sys.argv[1].isdigit():
  stdio.writeln("You must provide a number.")
  sys.exit()

size=int(sys.argv[1])
a=pascal(size)
for i in range(len(a)):
  for k in range(len(a[i])):
    stdio.write(str(a[i][k])+" ")
  stdio.writeln()