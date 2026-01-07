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
'''

while True:
    x = int(input('請輸入要提領的金額'))
    print(f'已提領{x}元')