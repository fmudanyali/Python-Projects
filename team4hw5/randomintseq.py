# Furkan MUDANYALI 20181701088
# Emir ÖZTÜRK 20181701062

import sys, random, stdio


def randomseq(x, y):
    a = []
    for i in range(y):
        a.append((random.randrange(x)))
    return a


a = randomseq(int(sys.argv[1]), int(sys.argv[2]))
for i in range(int(sys.argv[2])):
    print(a[i])
