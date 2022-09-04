def genFibbo(n):
    a1 = 1
    a2 = 1    
    for i in range(n):
        if i < 2:
            yield 1
        else:
            tmp = a1
            a1 = a2
            a2 = tmp + a2
            yield a2

for i in genFibbo(20):
    print(i)

def genFirst(n):
    for i in range(2, n+1):
        t = 0
        for j in range(1, i+1):
            if i % j == 0: t+= 1
        if t == 2:
            yield i

for i in genFirst(20):
    print(i)