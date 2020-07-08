from sympy import *
import numpy as np
x=symbols('x')

f = x**7-1000

g = diff(f,x)

def newton(x1,tol):
	a = x1
	b = a - (f.subs(x,a)/g.subs(x,a))
	while np.abs(a-b) >= tol :
	  a = b
	  if g.subs(x,a) != 0 :	
		b = a - f.subs(x,a)/g.subs(x,a)
	return a

root = newton(3.0,0.0000001)		

print "The root is",root