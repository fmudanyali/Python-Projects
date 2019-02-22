#!/usr/local/bin/python3
import stdio
#exports colors from colors.py
from colors import *
#assign a blank array
names = []
#read sortpeople.txt
group = open("sortpeople.txt","r+")
group = group.read().split("\n")
#do this size of sortpeople times
for i in range(len(group)):
    #divide the first line with , and append them into the names array
    set = str(group[i]).split(",")
    names.append(set)
    #your classic sorting algorithm
    for j in range(len(names)):
        currMin=j
        for k in range(j+1,len(names)):
            if names[currMin]>names[k]:
                currMin=k
        names[j],names[currMin]=names[currMin],names[j]
#omit the first element of the array as we started with blank
names=names[1:]
#print the sorted array line by line
for i in range(len(names)):
    print(GREEN+names[i][0]+RED+names[i][1]+YELLOW+names[i][2]+RESET)
