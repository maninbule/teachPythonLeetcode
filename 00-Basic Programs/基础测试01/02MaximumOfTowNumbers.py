
'''
给你两个整数，然返回较大的那个数
'''
def maximum(a:int, b:int)->int:
    if a > b:
        return a
    else:
        return b
    
print(maximum(1,10))