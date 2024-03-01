
'''
set的增加、查询、删除操作
'''
def set_operations():
    # 创建一个空集合
    my_set = set()

    # 添加元素
    my_set.add(1)
    my_set.add(2)
    my_set.add(3)

    # 查询元素
    if 1 in my_set:
        print("1 in my_set")
    else:
        print("1 not in my_set")

    # 删除元素
    my_set.remove(2)
    # 查询元素
    if 2 in my_set:
        print("2 in my_set")
    else:
        print("2 not in my_set")

    A = [1,2,3,3,4]
    st = set(A) # 把list转换成set，set自动去重

    L = list(st) # 把set转换成list

if __name__ == '__main__':
    set_operations()