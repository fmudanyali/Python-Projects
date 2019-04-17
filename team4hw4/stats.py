#!/usr/local/bin/python3
#Furkan MUDANYALI 20181701088
#Emir ÖZTÜRK 20181701062
import stdio,sys
array=[int(sys.argv[x]) for x in range(1,len(sys.argv))]
addition=0
for i in range(len(array)): addition+=array[i]
mean=addition/len(array)
addition=0
for i in range(len(array)): addition+=(array[i]-mean)**2
var=addition/len(array)
dev=var**0.5
stdio.writeln(mean)
stdio.writeln(var)
stdio.writeln(dev)