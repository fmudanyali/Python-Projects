#!/usr/local/bin/python3
#Furkan MUDANYALI 20181701088
#Emir ÖZTÜRK 20181701062

def normalize(x):
    for i in range(len(x)):
        if x[i]<0:
            return("Only positive floats are accepted. Please check your list.")
    minx,maxx=min(x),max(x)
    for i in range(len(x)):
        x[i]=(x[i]-minx)/(maxx-minx)
    return x

def main():
    a=[]
    print("Give me numbers to normalize, any string to stop.")
    while(1):
        try:
            a+=map(float,input().split(" "))
        except:
            print("String reached, calculating.")
            break
    print(normalize(a))

if __name__=='__main__': main()
