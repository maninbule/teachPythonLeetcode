
'''
初始化一个字典
'''

def initDict():
    Dict = {1: 'Geeks', 2: 'For', 3: 'Geeks'}
    print(Dict)

    Dict = {'Name': 'Geeks', 1: [1, 2, 3, 4]} # 字典中还可以嵌套其他类型
    print("\nDictionary with the use of Mixed Keys: ")
    print(Dict)



if __name__ == '__main__':
    initDict()