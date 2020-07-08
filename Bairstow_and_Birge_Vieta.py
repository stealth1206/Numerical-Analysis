from sympy import *
from sympy import degree
from sympy.abc import x
import numpy as np
import cmath
import random

print("Enter the expression in the form a*(x**n) + b*(x**m) + c*(x**j) ..... ")
exp = raw_input('Equation :')
expr = sympify(exp)
expression = Poly(expr)
coeff = expression.all_coeffs()
g = degree(expr)
print("Enter the choice of method to be used : \n 1) BAIRSTOW METHOD \n 2) BIRGE-VIETA METHOD")
choice = int(raw_input('Choice : ' ))

if(choice==1):
  coeff.reverse()
  def bairstow(a,r,s,g,roots):
	if(g<1):
		return None
	if((g==1) and (a[1]<>0)):
		roots.append(float(-a[0])/float(a[1]))
		return None
	if(g==2):
		D = (a[1]**2.0)-(4.0)*(a[2])*(a[0])
		X1 = (-a[1] - cmath.sqrt(D))/(2.0*a[2])
		X2 = (-a[1] + cmath.sqrt(D))/(2.0*a[2])
		roots.append(X1)
		roots.append(X2)
		return None
	n = len(a)
	b = [0]*len(a) #declaring a array of length len(a)
	c = [0]*len(a) #declaring a array of length len(a)
	b[n-1] = a[n-1]
	b[n-2] = a[n-2] + r*b[n-1]
	i = n-3
	while(i>=0):
		b[i] = a[i] + r*b[i+1] + s*b[i+2]
		i = i - 1
	c[n-1] = b[n-1]
	c[n-2] = b[n-2] + r*c[n-1]
	i = n-3
	while(i>=0):
		c[i] = b[i] + r*c[i+1] + s*c[i+2]
		i = i-1
	Din = ((c[2]*c[2])-(c[3]*c[1]))**(-1.0)
	r = r + (Din)*((c[2])*(-b[1])+(-c[3])*(-b[0]))
	s = s + (Din)*((-c[1])*(-b[1])+(c[2])*(-b[0]))
	if(abs(b[0])>0.0000001 or abs(b[1])>0.0000001):
		return bairstow(a,r,s,g,roots)
	if (g>=3):
		Dis = ((-r)**(2.0))-((4.0)*(1.0)*(-s))
		X1 = (r - (cmath.sqrt(Dis)))/(2.0)
		X2 = (r + (cmath.sqrt(Dis)))/(2.0)
		roots.append(X1)
		roots.append(X2)
	return bairstow(b[2:],r,s,g-2,roots)
  
  roots = []
  r = float(raw_input('Enter the first intial guess : '))
  s = float(raw_input('Enter the second intial guess : '))
  bairstow(coeff,r,s,g,roots)
  print(roots)

else :
   def b_vieta(x1,t):
	 x2 = 0
	 x = 1
	 while np.abs(x-x2)>=t :
	  b = coeff[0]
	  c = coeff[0]
	  for i in range(1,g) :
		b = coeff[i] + (x1)*b
		c = b + x1*c
	  b = coeff[g] + (x1)*b
	  x2 = x1 - (b/c)
	  x = x1
	  x1 = x2

	 return x
   r = float(raw_input('Enter the intial guess : '))
   print(b_vieta(r,0.0000001)) 
