'''
https://www.lintcode.com/problem/3141/?showListFe=true&page=1&problemTypeId=8&pageSize=50
'''

my_set = eval(input())
res = 0
for v in my_set:
    if abs(v) < 10:
        res += v
print(res)