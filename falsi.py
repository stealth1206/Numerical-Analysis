import numpy as np

def f(x) :
	return x**2 - x -1

def falsi(x1,x2,tol) :
	a = x1
	b = x2
	c = x1
	while np.abs(f(c)) >= tol :

	  c = b - f(b)*((b-a)/(f(b)-f(a)))
	  check1 = f(c)*f(a)
	  check2 = f(c)*f(b)
	  if check1 > 0 :
		a = c
	  else :
		if check2 > 0 :
		  b = c 

	return c

root = falsi(-2.0,0.0,0.0000001)
print "The root of equation by falsi is ",root	

