#!/usr/local/bin/python3
#Emir Öztürk      20181701062
#Furkan Mudanyalı 20181701088
import sys,stdio,math,time
prime=int(sys.argv[1])
#Initializing our array and dummy variable.
primes=[]
j="asd"
#just to see how long it takes
start=time.time()
#Check if the argument is <=3, if so, finish the program
#without any calculation.
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
#We all know 2 and 3 are primes.
primes.append(2)
primes.append(3)
#Start from 3, increase 2 by 2 for increible hihg sped.
#Since there is no reason to check for multiples of 2.
for i in range(3,prime+1,2):
    for k in range(2,int(i**0.5)+1):
        if i%k==0 and i!=k:
            #If this number can be divided perfectly, reset our
            #dummy variable and exit the loop.
            j="asd"
            break
        #Assign this number to our dummy.
        j=i
    #If our dummy hasn't been reset, append it to our primes array.
    if j!="asd":
        primes.append(j)
#Prints the desired value.
stdio.writeln(len(primes))
end=time.time()
#Prints the elapsed time.
print(str(round(end-start,3))+" Seconds")
