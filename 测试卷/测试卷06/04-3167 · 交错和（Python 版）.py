'''
https://www.lintcode.com/problem/3167/?showListFe=true&page=1&problemTypeId=8&pageSize=50
'''

# read data from console
n = eval(input())
# write your code here

res = 0
sign = -1
for i in range(1,n + 1):
    res += sign * i
    sign *= -1
print(res)