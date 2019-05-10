#!/usr/local/bin/python3
#Furkan MUDANYALI 20181701088
#Emir ÖZTÜRK 20181701062

import sys

def palindromeCheck(x):
    temp=""
    for i in range(len(x)-1,-1,-1):
        temp+=x[i]
    if temp==x:
        return True
    return False

def main(): print(palindromeCheck(sys.argv[1]))
if __name__=='__main__': main()