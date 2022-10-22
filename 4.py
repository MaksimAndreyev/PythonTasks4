from random import randint
with open('file.txt', 'w') as f:
    k = int(input())
    s = ''
    for i in range(k, 1, -1):
        q = randint(0, 100)
        if q == 0:
            continue
        s += str(q) + f'*x**{i} + '
    q = randint(0, 100)
    if q != 0:
        s += str(q) + '*x + '
    q = randint(0, 100)
    if q != 0:
        s += str(q)
    f.write(s+' = 0')
