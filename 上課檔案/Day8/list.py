'''
l = [1,2,3,4] #有
l1 = []#沒
if l: print(1)
if l1: print(2)

#3 -> True -1 -> True 0 -> False
#'hi' -> True '' -> False
#[1,2,3,4] -> True [''] -> True [] -> False

l = [i for i in range(10)]#[0,1,2,3,4,5,6,7,8,9]
print(l[0:])#start[init:0] end-1[len(l)-1] interval[init:1]
print(len(l))
print(max(l))
print(min(l))
print(sum(l))
#[0,3,6]

#length -> len
l = []
l.append(1)
l.append(2)
l.insert(0, 3)
a = l.pop()
l.remove(3)
print(l, a)
l = [1,2,3,4]
l.reverse()
print(sorted(l))
# l.sort()
print(l)
'''

l = [1,2,1,2,1,3,2,1]
print(l.count(2))
print(l.index(3))