#運算子 
'''
1.數學運算子 
num op num -> num
+, -, *, /, **(指數/次方), %(餘數), //（商數）

2**2 -> 2*2, 3*2 -> 3*3
print(4**2)
print(2**5)
print(20%6)
print(20//6)

-(負號) op num
print(-1+2)

2.邏輯運算子 num op num -> bool
>, <, >=, <=, ==(equal), !=(not equal)
print(4 > 1)
print(4 == '4')

3.布林運算子 bool op bool -> bool
(1)not 反閘
    周杰倫 Jay Chou:哎呦不錯喔 -> True
    不(not)錯(False) -> True
    錯  -> False

    不(not)行(True) -> False
    行  -> True

    print(not True)
    print(not False)

(2)or 或閘 （聯集）
    math or english -> 3000
    T       F          T
    F       T.         T
    T       T          T
    F       F          F 真值表Truth Table
    a = False
    b = False
    print(a or b)

(3)and 且閘 （交集）
    HW and 打掃 -> :)
    T.     F.     F
    F.     T.     F
    T.     T.     T
    F.     F.     F 真值表Truth Table
    a = False
    b = False
    print(a and b)

(4)xor[excursive or] 斥或閘 （差集）
    珍奶 xor 烏龍 -> :)
    T        F.     T
    F        T      T
    T        T.     F
    F        F.     F
    [1]not or and
    [2]binary
a = False
b = False
print((a or b) and not(a and b))
'''
print(input())