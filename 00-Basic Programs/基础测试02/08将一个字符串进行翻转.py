'''
08将一个字符串进行翻转

'1234'->'4321'

'1234' -> ['1','2','3','4']
->['4','3','2','1']
->'4321'
str -> list[str]
'''

def reverse(s:str)->str:
    A = [c for c in s]
    L,R = 0,len(A)-1
    while L < R:
        A[L],A[R] = A[R],A[L]
        L += 1
        R -= 1
    s2 = "".join(A)
    return s2
    

print(reverse("1234"))