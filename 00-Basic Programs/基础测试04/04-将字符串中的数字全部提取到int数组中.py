
'''
04-将字符串中的数字全部提取到int数组中

字符串中的数字用-来链接的
'''

def stringToArrInt(s:str)->list[int]:
    # A = s.split("-")
    # ans = []
    # for s in A:
    #     ans.append(int(s))
    # return ans
    # s.split("-") = ["123","1","4748","22","24"]
    return [int(n) for n in s.split("-")]

assert stringToArrInt("123-1-4748-22-24") == [123,1,4748,22,24]
assert stringToArrInt("123-1-4748") == [123,1,4748]
assert stringToArrInt("123") == [123]
print("pass")