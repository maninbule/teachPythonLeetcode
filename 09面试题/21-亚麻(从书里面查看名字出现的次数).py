'''
有一本书，有一些人的名字
我们要去这本书里面去看这些名字，分别出现了多少次

名字形式： lastName
'''

class Book:
    def __init__(self) -> None:
        self.name
    def getAllLines(self)-> list[str]:
        pass
# key:name, value: 次数
def solution(book:Book,names:list[str])->dict():
    count = dict()
    names = set(names)
    for line in book.getAllLines():
        newline = ""
        for c in line:
            if c.isalpha():
                newline += c
            else:
                newline += ' '
        arr = newline.split()
        for word in arr:
            if word in names:
                if word in count:
                    count[word] += 1
                else:
                    count[word] = 1
    return count
