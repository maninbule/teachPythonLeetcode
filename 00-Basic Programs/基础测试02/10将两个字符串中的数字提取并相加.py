
'''
10将两个字符串中的数字提取并相加

'1a2b3c'   '4e5f6g'

'123'   '456'

123 + 456 = 579
'''

def addFromString(s1:str,s2:str)->int:
    d1 = ""
    d2 = ""
    for c in s1:
        if c.isdigit():
            d1 += c
    for c in s2:
        if c.isdigit():
            d2 += c
    return int(d1) + int(d2)

print(addFromString('1a2b3c','4e5f6g'))