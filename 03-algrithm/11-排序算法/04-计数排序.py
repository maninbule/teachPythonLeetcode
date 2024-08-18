'''
O(n + maxvalue)
'''
# [0,10,100,1000,10,20]
A = [1,2,3,6,7,9,12,4,5,9,1,2,3,2,1]
maxvalue = max(A)
count = [0] * (maxvalue + 1)
for v in A: # O(n)
    count[v] += 1
ans = []
for i in range(0,maxvalue + 1): # O(maxvalue)
    for j in range(count[i]):
        ans.append(i)
print(ans)

# 通用quickSort O(nlogn)

# O(n + maxvalue)
