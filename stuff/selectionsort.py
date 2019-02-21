#!/usr/local/bin/python3
import stdio
#toSort = read from the file tosort.txt and place them in an array
toSort = open("tosort.txt","r+")
toSort = toSort.read().strip("\n").split(",")
toSort = list(map(int, toSort))
#i starts at 0, gets added 1 each loop, continues until its equal to toSort's size
for i in range(len(toSort)):
    #set our current minimum to the value of i
    currMin = i
    #j starts at i+1, gets added 1 each loop, continues until its equal to toSort's size
    for j in range(i+1,len(toSort)):
        #if current minimumth element of toSort is bigger than jth element of toSort,
        if toSort[currMin]>toSort[j]:
            #set our current minimum to j
            currMin = j
    #replace current minumumth element with ith element
    toSort[currMin],toSort[i]=toSort[i],toSort[currMin]
#i starts at 0, gets added 1 each loop, continues until its equal to toSort's size
for i in range(len(toSort)):
    #write ith element of toSort and add space
    stdio.write(str(toSort[i])+" ")
#add a line break when everything is finished
stdio.writeln()
