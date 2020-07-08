import numpy as np

def f(x) :
	return x**7-1000

def secant(x1,x2,tol) :
    a = x1
    c = x2
    
    while np.abs(a-c) >= tol :
    
       b = c - f(c)/((f(c)-f(a))/(c-a))
       a = c
       c = b
    
    return a
root = secant(2.0,3.0,0.00000001)
print "The root by secant method is :",root    
