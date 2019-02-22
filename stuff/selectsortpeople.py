#!/usr/local/bin/python3
import stdio
from colors import *
names = []
group = open("sortpeople.txt","r+")
group = group.read().split("\n")
for i in range(len(group)):
    set = str(group[i]).split(",")
    names.append(set)
    for j in range(len(names)):
        currMin=j
        for k in range(j+1,len(names)):
            if names[currMin]>names[k]:
                currMin=k
        names[j],names[currMin]=names[currMin],names[j]
names=names[1:]
for i in range(len(names)):
    print(GREEN+names[i][0]+RED+names[i][1]+YELLOW+names[i][2]+RESET)
