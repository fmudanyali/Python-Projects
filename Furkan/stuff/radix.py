#!/usr/local/bin/python3
import math
def countingSort(A,digit,radix):
  #Create list B which will be the sorted list.
  B=[0]*len(A)
  C=[0]*int(radix)
  #Counts the number of occurrences of each digit in A. 
  for i in range(len(A)):
    digitAi = int((A[i]/radix**digit)%radix)
    C[digitAi] = C[digitAi]+1
    #Now C[i] is the value of the number of elements in A equal to i.

  for j in range(1,radix):
    C[j] = C[j] + C[j-1]
  for m in range(len(A)-1, -1, -1):
    digitAi = int((A[m]/radix**digit)%radix)
    C[digitAi] = C[digitAi]-1
    B[C[digitAi]] = A[m]
  
  return B

def radixSort(A,radix):
  k = max(A)
  output = A
  digits = int(math.floor(math.log(k, radix)+1))
  for i in range(digits):
    output = countingSort(output,i,radix)
  return output

A = [9,3,1,4,5,7,7,2,20,55]
print(radixSort(A,10))