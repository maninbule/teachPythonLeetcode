

'''
01-将字符串中的所有单词首字母大写其余小写
每个单词是用一个空格隔开

'''

def UpperAllWordsInString(s:str)->str:
    # 切分 split
    words = s.split(" ")
    # 每个单词进行转换
    for i in range(len(words)): # ["hellO","WorLd"]
        w = ""
        for j in range(len(words[i])):
            if j == 0:
                w += words[i][j].upper()
            else:
                w += words[i][j].lower()
        words[i] = w
    # 将转换后的单词拼起来
    return " ".join(words)

assert UpperAllWordsInString("hellO WorLd") == "Hello World"
assert UpperAllWordsInString("hellO") == "Hello"
assert UpperAllWordsInString("hellO yes No") == "Hello Yes No"
print("pass")