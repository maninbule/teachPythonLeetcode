'''
https://www.lintcode.com/problem/3171/?showListFe=true&page=1&problemTypeId=8&pageSize=50
'''


def my_func(n:int,x:int)->(list[int],int):
    ans_list = []
    for i in range(1,n + 1):
        if i % x == 0:
            ans_list.append(i)
    return (ans_list,len(ans_list))

print(my_func(10,6))