#!/usr/local/bin/python3

print("Fizzbuzz Generator")

num1 = 3
num2 = 5
x = y = "jej"

while not x.isdigit():
    x = input("What's the number you wanna begin with?: ")
    if not x.isdigit():
        print("I want a number, try again.")
while not y.isdigit():
    y = input("What's the number you wanna end with?: ")
    if not y.isdigit():
        print("I want a number, try again.")
x = int(x)
y = int(y)

while x <= y:
    if x % (num1 * num2) == 0:
        print ("FizzBuzz!")
    elif x % num1 == 0:
        print ("Fizz!")
    elif x % num2 == 0:
        print ("Buzz!")
    else:
        print(x)
    x += 1
