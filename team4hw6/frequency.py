#!/usr/local/bin/python3
#Furkan MUDANYALI 20181701088
#Emir ÖZTÜRK 20181701062

def frequency(x):
    occur=[0]*10
    for i in range(10):
        for k in range(len(x)):
            if x[k]==i:
                occur[i]+=1
    return occur.index(max(occur))

def main():
    a=[]
    print("Give me single digits, string to stop.")
    while(1):
        try:
            a+=map(int,input().split(" "))
        except:
            print("String reached, calculating.")
            break
    print("The most frequent number is: "+str(frequency(a)))

if __name__=='__main__': main()