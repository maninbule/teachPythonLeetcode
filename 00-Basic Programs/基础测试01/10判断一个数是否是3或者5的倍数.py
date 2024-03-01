

'''
10判断一个数是否是3或者5的倍数

x % 2 == 1
x % 2 == 0

x % 3 == 0
x % 5 == 0
'''

def judge(x:int)->bool:
    if x % 3 == 0 or x % 5 == 0:
        return True
    else:
        return False
    

print(judge(15))