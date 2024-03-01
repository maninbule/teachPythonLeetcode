

'''
09将字符串中的所有数字提取出来成一个单独的字符串

把里面的所有的数字 加到一个新的字符串里面
'1a2b3c'

'123'
'''

def getDigitFromString(s:str)->str:
    ans = ""
    for c in s:
        if c.isdigit():
            ans += c
    return ans

print(getDigitFromString("1a2b3c"))