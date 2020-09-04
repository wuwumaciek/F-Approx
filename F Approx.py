import sympy
from sympy.utilities.lambdify import lambdify
from fractions import Fraction

def Convert(s):
    new = ""
    for x in s:
        new += x
    return new

def derivative(function, n):
    x = sympy.Symbol('x')
    f = function
    for y in range(n):
        f_temp = sympy.diff(f, x)
        f=f_temp
    return(f)

def silnia(n):
    if n>1:
        return n*silnia(n-1) 
    elif n in (0,1):
        return 1

#   print(derivative(input(), int(input())))

f = input()         #   funkcja
a = int(input())    #   dokładność
b = 0               
c = float(input())    #   miejsce
list1 = []
polynomial0 = []
polynomial = []

for n in range (a):
    x = sympy.Symbol('x')
    dx = (derivative(f, n))
    ddx = lambdify(x, dx)
    list1.append(ddx(c))
if(c==0):
    f=0
    for n in range (a):
        polynomial0.append(Fraction(int(list1[n]), int(silnia(n))))
        if int(list1[n]) != 0:
            if f==0 and n>0:
                if n>1:
                    temp = "(" + str(polynomial0[n]) + ")" + "x^" + str(n)
                    polynomial.append(temp)
                elif n == 1:
                    temp = "(" + str(polynomial0[n]) + ")" + "x"
                    polynomial.append(temp)
                elif n == 0:
                    temp = "(" + str(polynomial0[n]) + ")"
                    polynomial.append(temp)
            else:
                if n>1:
                    temp = " + (" + str(polynomial0[n]) + ")" + "x^" + str(n)
                    polynomial.append(temp)
                elif n == 1:
                    temp = " + (" + str(polynomial0[n]) + ")" + "x"
                    polynomial.append(temp)
                elif n == 0:
                    temp = "(" + str(polynomial0[n]) + ")"
                    polynomial.append(temp)
            f+=1

    out = Convert(polynomial)
    print(out)
else:
    f=0
    for n in range (a):
        #   print("%")
        #   print(list1[n])
        #   print(type(list1[n]))
        #   print("%")
        #   print(silnia(n))
        #   print(type(silnia(n)))
        #   print("%")
        #   print((list1[n])/(silnia(n)))
        polynomial0.append((list1[n])/(silnia(n)))
        
        if float(list1[n]) != 0:
            if f==0 and n>0:
                if n>1:
                    temp = "(" + str(polynomial0[n]) + ")" + "(x-" + str(c) + ")^" + str(n)
                    polynomial.append(temp)
                elif n == 1:
                    temp = "(" + str(polynomial0[n]) + ")" + "(x-" + str(c) + ")"
                    polynomial.append(temp)
                elif n == 0:
                    temp = "(" + str(polynomial0[n]) + ")"
                    polynomial.append(temp)
            else:
                if n>1:
                    temp = " + (" + str(polynomial0[n]) + ")" + "(x-" + str(c) + ")^" + str(n)
                    polynomial.append(temp)
                elif n == 1:
                    temp = " + (" + str(polynomial0[n]) + ")" + "(x-" + str(c) + ")"
                    polynomial.append(temp)
                elif n == 0:
                    temp = "(" + str(polynomial0[n]) + ")"
                    polynomial.append(temp)
            f+=1

    #   print(polynomial0)
    #   print(polynomial)
    #   print(f)
    out = Convert(polynomial)

    print(out)

