'''
# (5) 请你写一个class，实现一个简化版的图书管理系统，里面有以下功能：
    1. 添加一本书
    2. 借出一本书
    3. 用list[str]返回现在还没有被借出去的书
    4. 用list[str]返回现在被借出去的书
    5. 返回被借阅次数最多的3本书的名字

    另外：图书只用记录名字，每本图书的名字都不一样
'''
from collections import defaultdict
class BookManageMent:
    def __init__(self):
        self.havebook = dict()
        self.check_out_times = defaultdict(int)
    def addbook(self,title:str):
        self.havebook[title] = True
    def check_out_book(self,title:str):
        self.havebook[title] = False
        self.check_out_times[title] += 1
    def list_have_book(self)->list[str]:
        have = []
        for title,value in self.havebook.items():
            if value == True:
                have.append(title)
        return have
    def list_check_out_book(self)->list[str]:
        have = []
        for title,value in self.havebook.items():
            if value == False:
                have.append(title)
        return have
    def list_top3_book(self):
        check_out_book = []
        for key in self.check_out_times.keys():
            check_out_book.append(key)
        check_out_book.sort(key=lambda title:-self.check_out_times[title])
        return check_out_book[:min(3,len(check_out_book))]

bm = BookManageMent()
bm.addbook("bookA")
bm.addbook("bookB")
bm.addbook("bookC")
bm.addbook("bookD")
bm.addbook("bookE")
print(bm.list_have_book())
bm.check_out_book("bookB")
print(bm.list_have_book())
print(bm.list_check_out_book())
bm.addbook("bookB")
bm.check_out_book("bookB")
bm.check_out_book("bookA")
bm.addbook("bookA")
bm.check_out_book("bookE")
bm.check_out_book("bookD")
print(bm.list_top3_book())