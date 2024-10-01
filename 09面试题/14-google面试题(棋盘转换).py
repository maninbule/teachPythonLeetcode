'''

'''

'''
给两个棋盘的状态，问这两个棋盘的状态是否可以转化。
R可以向右走，L可以向左走
Given the states of two chessboards, ask whether the states of these two chessboards can be transformed.
R can go right, L can go left

注意：只能棋盘1向棋盘2转换
棋盘1: _R___L
棋盘2: __R_L_
输出yes


棋盘1: __L__R__L__L
棋盘2: _L____RLL___
输出yes

棋盘1: __R__R__L__R
棋盘2: _L____RLR___
输出no

棋盘1: __R__L
棋盘2: _R__L_
输出no

棋盘1: __L__R
棋盘2: _R__L_
输出no
'''

def judge(a:str,b:str)->bool:
    if len(a) != len(b):
        return False
    i ,j = 0,0
    while i < len(a) and j < len(b):
        while i < len(a) and a[i] == '_':
            i += 1
        while j < len(b) and b[j] == '_':
            j += 1
        if i == len(a) and j == len(b):
            return True
        if i == len(a) or j == len(b):
            return False
        # 都有棋子
        if a[i] != b[j]:
            return False
        if a[i] == 'L' and i < j:
            return False
        if a[i] == 'R' and i > j:
            return False
        i += 1
        j += 1
    return True

print(judge('_R___L','__R_L_'))
print(judge('__L__R__L__L','_L____RLL___'))
print(judge('__R__R__L__R','_L____RLR___'))
print(judge('__R__L','_R__L_'))
print(judge('__L__R','_R__L_'))
print(judge('RRR___','___RRR'))
print(judge('RL___','_RL__'))