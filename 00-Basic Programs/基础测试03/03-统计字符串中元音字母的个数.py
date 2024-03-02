

'''
03-统计字符串中元音字母的个数
元音字母有：a e i o u 及其大写
字符串中包含了大写字母和小写字母,以及其他字符
'''

def count(s:str)->int:
    # cnt = 0
    # for c in s:
    #     if c == 'a' or c == 'e'or c == 'i' or c == 'o' or c == 'u':
    #         cnt += 1
    #     elif c == 'A' or c == 'E'or c == 'I' or c == 'O' or c == 'U':
    #         cnt += 1
    # return cnt
    # ----------------第二种
    # cnt = 0
    # for c in s:
    #     if c in ['a','e','i','o','u','A','E','I','O','U']:
    #         cnt += 1
    # return cnt
    # --------------- 第三种
    cnt = 0
    for c in s:
        if c in "aeiouAEIOU":
            cnt += 1
    return cnt

assert count("hEllo world") == 3
assert count("gIthub") == 2
print("pass")