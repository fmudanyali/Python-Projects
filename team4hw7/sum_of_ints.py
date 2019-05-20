#!/usr/local/bin/python3
#Furkan MUDANYALI 20181701088
#Emir ÖZTÜRK 20181701062
import sys

def sum_iter(n):
    x=0
    for i in range(1,n+1): x+=i
    return x

def sum_rec(n):
    if n == 1: return n
    return n+sum_rec(n-1)

def main():
    print(sum_iter(int(sys.argv[1])))
    print(sum_rec(int(sys.argv[1])))

if __name__=='__main__': main()