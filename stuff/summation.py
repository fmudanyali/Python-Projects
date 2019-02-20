#!/usr/local/bin/python3
print("Add numbers from X to Y")
x = y = "string" # make them string so theyre stuck in the while loop
z = 0
while not x.isdigit():
    x = input("What is X?: ")
    if not x.isdigit(): # refuses string values
        print("Please give me a number.")
x = int(x)
while not y.isdigit() or int(y) <= x:
    y = input("What is Y?: ")
    if not y.isdigit(): # refuses string values
        print("Please give me a number.")
    elif int(y) <= x: # if it is an integer, checks if it is smaller than or equal to x
        print("Y can't be smaller than or equal to X")
y = int(y)
while x <= y: # the addition algorithm
    z = z+x
    x = x+1
print(z)
