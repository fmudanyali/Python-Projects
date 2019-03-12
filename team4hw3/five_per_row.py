#!/usr/local/bin/python3
#Emir Öztürk      20181701062
#Furkan Mudanyalı 20181701088
import stdio
def five_per_row(x,y):
    for i in range (x,y):
        stdio.write(str(i)+" ")
        if i%5==0:stdio.writeln("")

five_per_row(101,201)
