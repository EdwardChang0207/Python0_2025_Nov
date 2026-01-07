a, b, c = input().split() #'1 0 0' -> ['1', '0', '0']
#string -> integer int()
a, b, c = int(a), int(b), int(c)
D = b**2 - 4*a*c
#case3. 無解
if D < 0: print('No real root')
else:
    x1 = int((-b+D**0.5)//(2*a))
    x2 = int((-b-D**0.5)//(2*a))

    #case1. 兩相異解
    if D > 0:
        print('Two different roots x1='+str(x1) , ', x2='+str(x2))
    #case2. 兩相同解
    elif D == 0:
        print('Two same roots x='+str(x1))
    