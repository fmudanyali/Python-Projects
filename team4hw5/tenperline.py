# Furkan MUDANYALI 20181701088
# Emir ÖZTÜRK 20181701062

import sys, stdio

a = []
while not stdio.isEmpty():
    a.append(stdio.readInt())

for i in range(100):
    if i % 10 == 0:
        print("")
    sys.stdout.write(str(a[i]) + " ")
print("")
