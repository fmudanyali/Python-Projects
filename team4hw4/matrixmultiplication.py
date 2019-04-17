#!/usr/local/bin/python3
#Furkan MUDANYALI 20181701088
#Emir ÖZTÜRK 20181701062
import sys,stdio,random
def matrixMulti(row_A,col_A,row_B,col_B):
  if col_A!=row_B:
    stdio.writeln("The number of columns in the first matrix must be equal to the number of rows in second matrix.")
    sys.exit()
  A=[[round(random.uniform(0,100),2) for i in range(col_A)] for k in range(row_A)]
  B=[[round(random.uniform(0,100),2) for i in range(col_B)] for k in range(row_B)]
  C=[[0.0 for i in range(col_B)] for k in range(row_A)]
  for i in range(row_A):
    for j in range(col_B):
      for k in range(col_A):
        C[i][j] += A[i][k]*B[k][j]
  return A,B,C

#Failproofing
if len(sys.argv)<4:
  stdio.writeln("You must provide 4 arguments.")
  sys.exit()
for i in range(1,5):
  if not sys.argv[i].isdigit():
    stdio.writeln("You must provide numbers.")
    sys.exit()

A,B,C=matrixMulti(int(sys.argv[1]),int(sys.argv[2]),int(sys.argv[3]),int(sys.argv[4]))

for i in range(len(A)): stdio.writeln(A[i])
stdio.writeln()
for i in range(len(B)): stdio.writeln(B[i])
stdio.writeln()
for i in range(len(C)): stdio.writeln(C[i])