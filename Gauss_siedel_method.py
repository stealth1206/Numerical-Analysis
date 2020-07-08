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

def Gauss_Seidel(A, b, error_s):
	[m, n] = np.shape(A)
	U = np.triu(A, 1)
	L = np.tril(A)
	x = np.ones((m,1))
	err = np.ones((m,1))*100
	while np.max(err) > error_s:
		xn = np.dot(np.linalg.inv(L), (b - np.dot(U, x)))
		err = abs((xn - x)/xn)*100
		x = xn
	for i in range(0, m):
		print 'x[%0.0f] = %6.4f' % (i+1, x[i]) 

error_s = 5 
Gauss_Seidel(a, b, error_s)