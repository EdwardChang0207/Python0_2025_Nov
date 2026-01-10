N = int(input())
for i in range(N):
    a, b, c = [int(i) for i in input().split()]
    if a == 1: print(b+c)
    elif a == 2: print(b-c)
    elif a == 3: print(b*c)
    else: print(b//c)