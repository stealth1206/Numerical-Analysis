import numpy as np

def f(x) :
   
   return x**3 - 1

def bisection(a,b,tol) :
   
   l = a
   r = b
   while np.abs(l-r)>=tol :
     c= l+r/2.0
     check = f(l)*f(c)   
     if check > tol :
     	l = c
     else :
     	if check < tol :
          r = c
   return c 

root = bisection(0.0,2.0,0.1)
print "Root :" + root       	

