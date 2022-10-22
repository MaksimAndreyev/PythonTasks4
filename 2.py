N = int(input('Введите число: '))
a = []
for i in range(2, N+1):
    if N == 1:
        break
    while N % i == 0:
        N //= i
        a.append(i)
print(*a)
