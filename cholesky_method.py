import numpy as np
from math import sqrt

print("Enter the size of Array of which you have to find LU-Decomposition : ")
n = int(input())
print("Enter the elements of array by pressing ENTER key after typing each entry : ")
a = np.zeros((n,n))
for i in range(0,n):
	for j in range(0,n):
		a[i][j]=int(input())

def cholesky(A,n):
   L = np.zeros((n,n))
   for i in range(n): # Perform the Cholesky decomposition
      for k in range(i+1):
         temp_sum = sum(L[i][j] * L[k][j] for j in range(k)) 
         if (i == k): # Diagonal elements
            L[i][k] = sqrt(A[i][i] - temp_sum)
         else:
            L[i][k] = (1.0 / L[k][k] * (A[i][k] - temp_sum))
   return L

print("Lower-Triangular matrix founded by cholexky method is : "+str(cholesky(a,n)))