#!/usr/local/bin/python3
#Furkan MUDANYALI 20181701088
#Emir ÖZTÜRK 20181701062
import random,stdio

def matrixTrans(w=3,h=10):
  matrix=[[random.randrange(0,100) for i in range(w)] for k in range(h)]
  matrixT=[[None for i in range(h)] for k in range(w)]
  for i in range(w):
    for k in range(h):
      matrixT[i][k]=matrix[k][i]
  return matrix,matrixT

matrix,matrixT=matrixTrans()
for i in range(len(matrix)): stdio.writeln(matrix[i])
stdio.writeln()
for i in range(len(matrixT)): stdio.writeln(matrixT[i])