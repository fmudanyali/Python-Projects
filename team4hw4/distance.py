#!/usr/local/bin/python3
#Furkan MUDANYALI 20181701088
#Emir ÖZTÜRK 20181701062
import stdio,sys
x=[1,3]
y=[2,5]
dist=0
for i in range(len(x)):
  dist+=(x[i]-y[i])**2
dist=dist**0.5
stdio.writeln(dist)