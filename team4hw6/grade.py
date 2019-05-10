#!/usr/local/bin/python3
#Furkan MUDANYALI 20181701088
#Emir ÖZTÜRK 20181701062

def score(x):
    return (float(x[0])*30/100)+(float(x[1])*30/100)+(float(x[2])*40/100)

def letterGrade(x):
    if x>100: return "Value too high."
    if x<=100 and x>=85: return "AA"
    if x<85 and x>=75: return "BA"
    if x<75 and x>=70: return "BB"
    if x<70 and x>=65: return "CB"
    if x<65 and x>=60: return "CC"
    if x<60 and x>=55: return "DC"
    if x<55 and x>40: return "DD"
    if x<40 and x>=0: return "FF"
    if x<0: return "Value too low."

def main():
    print("Input 3 numbers.")
    z=[]
    while len(z)<3:
        try:
            z+=map(int,input().split())
        except:
            print("Please input numbers.")
    x=score(z)
    print("Your score is: "+str(x))
    print("Your letter grade is: "+letterGrade(x))

if __name__=='__main__': main()