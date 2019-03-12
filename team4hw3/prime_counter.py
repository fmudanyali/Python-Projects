#!/usr/local/bin/python3
#Emir Öztürk      20181701062
#Furkan Mudanyalı 20181701088
import sys,stdio,time
def doPrime(x):
    #Initializing our array.
    primes=[]
    #just to see how long it takes
    start=time.time()
    #Check if the argument is <=3, if so, finish the program
    #without any calculation.
    if x==3:
        primes.append(2)
        primes.append(3)
        stdio.writeln(len(primes))
        sys.exit()
    elif x==2:
        primes.append(2)
        stdio.writeln(len(primes))
        sys.exit()
    elif x<2:
        stdio.writeln("none")
        sys.exit()
    #We all know 2 is a prime.
    primes.append(2)
    #Start from 3, increase 2 by 2 for increible hihg sped.
    #Since there is no reason to check for even numbers.
    for i in range(3,x+1,2):
        #Initialize condition.
        j=True
        for k in range(3,int(i**0.5)+1,2):
            if i%k==0 and i!=k:
                #If this statement is true, change our condition to false.
                j=False
                break
        #Assign i if our condition is true.
        if j:primes.append(i)
    #Prints the desired value.
    stdio.writeln(len(primes))
    end=time.time()
    #Prints the elapsed time.
    print(str(round(end-start,3))+" Seconds")

if len(sys.argv)<2:stdio.writeln("Please give me an argument.")
else:doPrime(int(sys.argv[1]))
