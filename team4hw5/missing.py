# Furkan MUDANYALI 20181701088
# Emir ÖZTÜRK 20181701062

import sys, stdio


def missingNumber(number):
    a = b = []
    x = y = 0
    for i in range(1, number + 1):
        x += i

    while not stdio.isEmpty():
        b.append(stdio.readInt())

    if len(b) != number - 1:
        print("You must enter " + str(number) + " numbers.")
        sys.exit()

    for i in range(len(b)):
        y += b[i]

    return x - y


missing = missingNumber(int(sys.argv[1]))
stdio.writeln("Missing number:")
stdio.writeln(missing)
