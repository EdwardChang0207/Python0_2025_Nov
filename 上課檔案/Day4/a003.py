#input
date = input().split() #'1 1' -> ['1', '1']
m = int(date[0])
d = int(date[1])
s = (m*2+d)%3
l = ['普通','吉','大吉']
print(l[s])
