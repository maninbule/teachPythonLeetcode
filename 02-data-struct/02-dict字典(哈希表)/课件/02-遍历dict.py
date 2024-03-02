
'''
遍历dict
'''

def trverseDict():
    my_dict = {'a': 1, 'b': 2, 'c': 3}
    # 只遍历key
    for key in my_dict.keys():
        print(key,end=" ")
    print()
    # 只遍历value
    for value in my_dict.values():
        print(value,end=" ")
    print()
    # 同时遍历key和value
    for key, value in my_dict.items():
        print("(",key, value,end=" ) ")

if __name__ == '__main__':
    trverseDict()

    s = ["wrold","wrold","abc","abc","def"]
    mp = dict()
    for word in s:
        if word not in mp:
            mp[word] = 1
        else:
            mp[word] += 1
    print(mp)

