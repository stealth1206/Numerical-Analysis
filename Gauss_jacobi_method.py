import numpy as np

n = int(input())
a = np.zeros((n,n))
for i in range(0,n):
	for j in range(0,n):
		a[i][j]=int(input())
print("Enter the matrix containing all values : ")
b = np.zeros((n,1))
for i in range(0,n):
	b[i] = int(input())
print("Enter the intial guess : ")
x = np.zeros((n,1))
for i in range(0,n):
	x[i] = int(input())

def jacobi(A,b,x):                                                                                                                                                                         
    D = np.diag(A)
    R = A - np.diagflat(D)                                                                                                                                                                          
    while np.linalg.norm(np.matmul(A,x)-b,2)>0.0001:
        x = (b-np.matmul(R,x)) / D
    return x
sol = jacobi(a,b,x)
print("Solution"+str(sol))