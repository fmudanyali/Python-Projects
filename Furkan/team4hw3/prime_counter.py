#!/usr/local/bin/python3
#Emir Öztürk      20181701062
#Furkan Mudanyalı 20181701088
import sys,stdio,math,time
prime=int(sys.argv[1])
primes=[]
j="asd"
start=time.time()
if prime==3:
    primes.append(2)
    primes.append(3)
    stdio.writeln(primes)
    sys.exit()
elif prime==2:
    primes.append(2)
    stdio.writeln(primes)
    sys.exit()
elif prime<2:
    stdio.writeln("none")
    sys.exit()
primes.append(2)
primes.append(3)
for i in range(3,prime+1,2):
    for k in range(2,int(i**0.5)+1):
        if i%k==0 and i!=k:
            j="asd"
            break
        j=i
    if j!="asd":
        primes.append(j)
stdio.writeln(len(primes))
end=time.time()
print(str(round(end-start,3))+" Seconds")
