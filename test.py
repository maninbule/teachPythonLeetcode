

# 类 概念 -> 具体下来就是一个对象
class Student:
    # 构造函数
    def __init__(self,id:str,name:str,score:int): # 成员函数
        self.id = id # 成员变量
        self.name = name
        self.score = score
    def __str__(self): # 需要返回一个字符串
        return self.id + ": " + self.name + "总分: " + str(self.score)
    def change(self):
        self.score -= 1

stu = Student("10001","Lee",100)
stu.change()
print(stu)
B = Student("10002","Peter",90)
print(B)

print(type(stu),type(B),type(123),type("123"))