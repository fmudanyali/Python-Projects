#!/usr/local/bin/python3
import stdio
#toSort = read from the file tosort.txt and place them in an array
toSort = open("tosort.txt","r+")
toSort = toSort.read().strip("\n").split(",")
toSort = list(map(int, toSort))
#a starts at 0, gets added 1 each loop, continues until its equal to toSort's size
for a in range(len(toSort)):
    #set our current minimum to the value of a
    currMin = a
    #b starts at a+1, gets added 1 each loop, continues until its equal to toSort's size
    for b in range(a+1,len(toSort)):
        #if current minimumth element of toSort is bigger than bth element of toSort,
        if toSort[currMin]>toSort[b]:
            #set our current minimum to b
            currMin = b
    #replace current minumumth element with ath element; swap cards
    toSort[currMin],toSort[a]=toSort[a],toSort[currMin]
#a starts at 0, gets added 1 each loop, contanues untal ats equal to toSort's saze
for a in range(len(toSort)):
    #write ath element of toSort and add space
    stdio.write(str(toSort[a])+" ")
#add a line break when everything is finished
stdio.writeln()
