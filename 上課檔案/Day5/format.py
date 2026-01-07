'''
format: 1.str & int & other組合 2.對齊 3.四捨五入or取小數後第幾位

格式符號
%s(str) 
%d(int)
%f(float)

ex. my name is {name}, and I am {age} years old.
(1) %
(2) format
(3) f-string (function)
name = 'kevin'
age = 18
print('my name is', name, ', and I am', age, 'years old.')
print('my name is %s, and I am %d years old.' % (name, age))
print('my name is {}, and I am {} years old.'.format(name, age))
print(f'my name is {name}, and I am {age} years old.')
# print(input('請輸入姓名'))

name = ['kevin','andy','joe']
age = [20, 9, 100]

print('my name is %5s, and I am %3d years old.' % (name[0], age[0]))
print('my name is {:5s}, and I am {:3d} years old.'.format(name[1], age[1]))
print(f'my name is {name[2]:5s}, and I am {age[2]:3d} years old.')
'''

pi = 3.14159
print('%.2f'%pi)
print('{:.2f}'.format(pi))
print(f'{pi:.2f}')

