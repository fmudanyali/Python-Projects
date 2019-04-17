#!/usr/local/bin/python3
#Furkan MUDANYALI 20181701088
#Emir ÖZTÜRK 20181701062
import stdio,sys
size=int(sys.argv[1])
if size<0:
  stdio.writeln("Size cannot be smaller than 0.")
  sys.exit()
a=[[1 for i in range(k+1)] for k in range(size+1)]
for i in range(size+1):
  for k in range(1,i):
    a[i][k]=a[i-1][k-1]+a[i-1][k]
for i in range(len(a)):
  for k in range(len(a[i])):
    stdio.write(str(a[i][k])+" ")
  stdio.writeln()