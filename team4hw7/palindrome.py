#!/usr/local/bin/python3
#Furkan MUDANYALI 20181701088
#Emir ÖZTÜRK 20181701062
import sys

def is_palindrome(str,x,y):
    if x==y: return True
    if str[x]!=str[y]: return False
    if x<y+1: is_palindrome(str,x+1,y-1)
    return True
    
def main():
    str=sys.argv[1]
    print(is_palindrome(str,0,len(str)-1))

if __name__=='__main__': main()