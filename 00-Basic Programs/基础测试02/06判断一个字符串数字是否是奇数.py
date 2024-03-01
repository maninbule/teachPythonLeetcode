

'''
06判断一个字符串数字是否是奇数

'123' != 123
'''

def judgeOdd(x:str)->bool:
    y = int(x) # '123' int('123') -> 123
    if y % 2 == 1:
        return True
    else:
        return False
    
print(judgeOdd('122'))