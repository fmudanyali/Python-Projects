#!/usr/local/bin/python3

# Fizzbuzz is a game which you replace 2 numbers, and the multiple of those numbers
# with Fizz and Buzz, and FizzBuzz if the number is multiple of those 2 numbers.
print("Fizzbuzz Generator")

num1 = 3 #our 2 numbers
num2 = 5
x = y = "jej" #just assigning some random string for user input.
#also x and y are our starting and finishing points.
while not x.isdigit(): #repeat this process while x is not a digit.
    x = input("What's the number you wanna begin with?: ")
    if not x.isdigit(): #if user enters a string, execute this.
        print("I want a number, try again.")
while not y.isdigit(): #repeat this process while y is not a digit.
    y = input("What's the number you wanna end with?: ")
    if not y.isdigit(): #if user enters a string, execute this.
        print("I want a number, try again.")
x = int(x) #convert the strings which only contain numbers to integers.
y = int(y)

while x <= y: #while x is smaller or equal than y, do this.
    if x % (num1 * num2) == 0: #if the number divides perfectly by num1*num2
        print ("FizzBuzz!")
    elif x % num1 == 0: #else if the number divides perfectly by num1
        print ("Fizz!")
    elif x % num2 == 0: #else if the number divides perfectly by num2
        print ("Buzz!")
    else: #if nothing else works, just print out the number
        print(x)
    x += 1 #add 1 to x
