#!/usr/local/bin/python3
import stdio
toSort = open("tosort.txt","r+")
toSort = toSort.read().strip("\n").split(",")
toSort = list(map(int, toSort))
for i in range(len(toSort)):
    currMin = i
    for j in range(i+1,len(toSort)):
        if toSort[currMin]>toSort[j]:
            currMin = j
    toSort[currMin],toSort[i]=toSort[i],toSort[currMin]
for i in range(len(toSort)):
    stdio.write(str(toSort[i])+" ")
stdio.writeln()
