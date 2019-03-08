#!/usr/local/bin/python3
import sys,stdio,math
prime=int(sys.argv[1])
primes=[]
j="asd"
for i in range(2,prime):
    for k in range(2,i+1):
        if i%k==0 and not i==k:
            j="asd"
            break
        else:
            k+=1
            j=i
    if j!="asd":
        primes.append(j)
stdio.writeln(len(primes))
