from sympy import simplify
with open('polynomial1.txt') as f:
    a = f.readline()
with open('polynomial2.txt') as f:
    b = f.readline()
with open('sum.txt', 'w') as f:
    s = simplify(a+' + '+b)
    f.write(str(s))
