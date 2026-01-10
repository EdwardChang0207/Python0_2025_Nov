'''
天數: 1 2 3 ... n
饅頭: a, b, c, ...

day1: 第一天饅頭一顆的錢 * 買幾顆 = 第一天花多少錢
day2: 第2天饅頭一顆的錢 * 買幾顆 = 第2天花多少錢

day1+day2+day3+...+dayn

range(start[init:0], end, interval[init:1])
數字範圍
1~n

[a, b, c]
 0. 1. 2
'''
n = int(input())
c = input().split()
#['1','2','3',...]
#. 0.  1.  2
r = 0
for i in range(1, n+1):#i:1~n 第i天饅頭一顆的錢
    r += int(c[i-1])*i#第i天花多少錢
print(r)
