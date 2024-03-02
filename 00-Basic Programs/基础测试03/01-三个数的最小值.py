
'''
给你三个数，求这三个数的最小值
'''

def getMinOfTreeNumbers(a:int,b:int,c:int)->int:
    # if a < b:# b 不是最小值，最小值只会在a,c之间
    #     if a < c:
    #         return a
    #     else:
    #         return c
    # else: # a > b 此时a一定就不是最小值
    #     if b < c:
    #         return b
    #     else:
    #         return c
    # ----------------------
    # if a <= min(b,c):return a
    # if b <= min(a,c):return b
    # return c
    #-----------------------
    arr = [a,b,c]
    arr.sort()
    return arr[0]


assert getMinOfTreeNumbers(3,1,2) == 1
assert getMinOfTreeNumbers(1,1,1) == 1
assert getMinOfTreeNumbers(2,1,1) == 1
print("pass")