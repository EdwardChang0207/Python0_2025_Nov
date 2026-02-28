def expend_map(map):
    row_len = len(map[0])+2
    for i in range(len(map)):
        map[i].insert(0,'')
        map[i].append('')
    map.insert(0,['']*row_len)
    map.append(['']*row_len)
    return map
while True:
    m = [
        ['','',''], #0
        ['','',''], #1
        ['','','']  #2
    ]#.   0  1. 2
    steps = []
    game = True
    player = 'O'
    while game:
        for i in range(len(m)):
            print(m[i])
        a, b = [int(i) for i in input().split()]
        if m[a][b]: 
            print('請勿重複選取')
            continue
        m[a][b] = player
        steps.append([a,b])

        for i in range(3):
            if m[i].count(player) == 3:
                print(f'{player} Won!')
                game = False
                break
            if m[0][i] == m[1][i] == m[2][i] == player:
                print(f'{player} Won!')
                game = False
                break
        if m[0][0] == m[1][1] == m[2][2] == player:
            print(f'{player} Won!')
            game = False
        if m[0][2] == m[1][1] == m[2][0] == player:
            print(f'{player} Won!')
            game = False
        
        space = 0
        for i in m:
            space += i.count('')
        if space == 0:
            m = expend_map(m)
        
        # if space <= 2:
        #     a, b = steps.pop(0)
        #     m[a][b] = ''

        if player == 'O': player = 'X'
        else: player = 'O'
    if input('continue? y/n') == 'n': break


'''
鍵盤輸入： 
    2 2 -> m[2][2] = O
    0 2 -> m[0][2] = O

R1:O, R2:X, R3:O, R4:X, ...
'''
#queue 佇列
#l = [[0,0],[1,0], ...]
#a, b = l.pop(0)


'''
1.棋盤擴大
2.在平手前把第一步消失

[O,'','',X]
['',O,X,'']
['',X,O,'']
[X,'','',O]

'''