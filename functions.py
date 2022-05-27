from sympy import symbols, solve, lambdify
import numpy as np

def trans_quad(a,b,c):
    x = symbols('x')
    return a * x**2 + b*x + c
    

def compute_roots(quad):
    return solve(quad)
    #listroots = [key for key in roots_zer.keys()]
    #return listroots
print(compute_roots(trans_quad(2,-1,-1)))

def obtainequation(eq,range_x):
    x = symbols('x')
    tr = lambdify(x,eq,'numpy')
    return tr(range_x)


#range_x = np.linspace(-10,10,100)
#print(obtainequation(trans_quad(1,2,3),range_x))






