n = int(input())
for i in range(n):
    #一個對聯的判斷
    l1 = input().split()
    l2 = input().split()
    r = ''
    #A
    '''
    if l1[1] == l1[3] or l1[1] != l1[5]:
    if l2[1] == l2[3] or l2[1] != l2[5]:
    '''

    for l in [l1, l2]:
        if l[1] == l[3] or l[1] != l[5]:
            r += 'A'
            break

    #B
    if l1[-1] == '0' or l2[-1] == '1':
        r += 'B'
    #C
    '''
    if l1[1] == l2[1] or l1[3] == l2[3] or l1[5] == l2[5]:
    '''
    for i in range(1, 6, 2):#1, 3, 5
        if l1[i] == l2[i]:
            r += 'C'
            break
    if r:
        print(r)
    else:
        print('None')