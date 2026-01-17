n = int(input())
s = [int(i) for i in input().split()]
s.sort()
for i in range(len(s)):
    if i == len(s)-1:
        print(i)
    else:    
        print(i, end=' ')

if s[-1] < 60:
    print(s[-1])
    print('worst case')
elif s[0] >= 60:
    print('best case')
    print(s[0])
else:
    for i in range(len(s)):
        if s[i] >= 60:
            print(s[i-1])
            print(s[i])