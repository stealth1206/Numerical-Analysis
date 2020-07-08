import numpy as np

print("Enter the size of Array of which you have to find LU-Decomposition : ")
n = int(input())
print("Enter the elements of array by pressing ENTER key after typing each entry : ")
a = np.zeros((n,n))
for i in range(0,n):
	for j in range(0,n):
		a[i][j]=int(input())

print("Enter the choice of method to be used : \n 1) CROUT METHOD \n 2) DOOLITLE METHOD")
choice = int(raw_input('Choice : ' ))

if(choice == 1):
  def crout(A,n) :
	L = np.zeros((n,n))
	U = np.zeros((n,n))

	for i in range(n):
		U[i][i]=1
		for j in range(i,n):
			sum0 = A[j][i]	
			for k in range(i):
				sum0 -= L[j][k]*U[k][i]
			L[j][i] = sum0
			print(L[j][i])
		for j in range(i+1,n):
			sum1 = A[i][j]
			for k in range(i):
			   sum1 -= L[i][k]*U[k][j]
			U[i][j] = sum1/L[i][i]

	print("Lower-Triangular Matrix is : "+str(L))
	print("Upper-Triangular Matrix is : "+str(U))
		  
  crout(a,n) 

elif(choice==2):
	
 def doolittle(A,n) :
	L = np.zeros((n,n))
	U = np.zeros((n,n))

	for i in range(n):
		L[i][i]=1
		for k in range(i,n):
			sum0 = 0	
			for j in range(i):
				sum0 += (L[i][j]*U[j][k])
			U[i][k] = A[i][k]-sum0
		for k in range(i+1,n):
			sum1 = 0
			for j in range(i):
			   sum1 += (L[k][j]*U[j][i])
			L[k][i] = (A[k][i]-sum1)/U[i][i]

	print("Lower-Triangular Matrix is : "+str(L))
	print("Upper-Triangular Matrix is : "+str(U))
		  
 doolittle(a,n)   

