#!/usr/local/bin/python3
#Furkan MUDANYALI 20181701088
#Emir ÖZTÜRK 20181701062
import random,sys,stdio
SUITS=['Clubs','Diamonds','Hearts','Spades']
RANKS=['2','3','4','5','6','7','8','9','10','Jack','Queen','King','Ace']
rank=random.randrange(0,len(RANKS))
suit=random.randrange(0,len(SUITS))
deck=[]
for rank in RANKS:
  for suit in SUITS:
    card=rank+' of '+suit
    deck+=[card]
n=len(deck)
for i in range(n):
  r=random.randrange(i,n)
  deck[i],deck[r]=deck[r],deck[i]
hands=[["" for k in range(5)] for i in range(int(sys.argv[1]))]
for k in range(5):
  for i in range(int(sys.argv[1])):
    r=random.randrange(0,len(deck))
    hands[i][k]+=deck[r]
for i in range(len(hands)): stdio.writeln(hands[i])