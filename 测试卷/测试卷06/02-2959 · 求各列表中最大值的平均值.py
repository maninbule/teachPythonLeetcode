'''
https://www.lintcode.com/problem/2959/?showListFe=true&page=1&problemTypeId=8&pageSize=50
'''

list_1 = eval(input())
# Please your code here
total = 0
cnt = len(list_1)
for L in list_1:
    total += max(L)
print("%.2f"%(total/cnt))
