import sympy
from sympy.utilities.lambdify import lambdify
from math import factorial as silnia

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

print(list1)
f=0
for n in range (a):
    polynomial0.append((float(list1[n]))/(float(silnia(n))))
    if float(list1[n]) != 0:
        if f==0 and n>0:
            if n>1:
                temp = "(" + str(polynomial0[n]) + ")" + "x^" + str(n)
                polynomial.append(temp)
            elif n == 1:
                temp = "(" + str(polynomial0[n]) + ")" + "x"
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
print(polynomial0)
out = Convert(polynomial)
print(out)
