'''
print(1)
print(2)
print(3)

while <條件>:
    ...

[鮭魚,鮪魚,玉子燒] 
    
for

index 索引值

i = 1
while i <= 16:
    print(i)
    i *= 2

for sushi in ['鮭魚','鮪魚','玉子燒']:
    print(sushi)

range(start[init:0], end, interval[init:1])
start -> end-1, +interval

10 -> 1
for i in range(10, 0, -1):
    print(i)
   
for -> while ?  O
while -> for ?  O
    
l = [1, 5, 2, 4, 102]
i = 0
while i <= 4:
    print(l[i])
    i += 1

while True:
    x = int(input('請輸入要提領的金額'))
    print(f'已提領{x}元')

綜合表達式
[1,2,3,4,5,6,7,...]

[放在list裡面的東西 for i in range()]
[1,2,3,4,5,6,7]
[2,4,6,8,10,12,14]
# [1,4,9,16,25,36,49]
print([i*i for i in range(1,8)])   
print([i**2 for i in range(1,8)])    

[1,1,1,1,1,1,1,1,1,1]
[1,1,1,1,1,1,1,1,1,1]
print([1 for i in range(10)])

[0,1,2,3,4,5,6,7,8,9]
[0,1,2,0,1,2,0,1,2,0]

# [0,1,2,0,1,2,0,1,2]
print([i for i in range(3)]*3)
print([i%3 for i in range(9)])

'1 2 3' -> ['1','2','3']
[1, 2, 3]
'''
[int(i) for i in input().split()]