'''
O(n^2)
'''

A = [1,2,3,6,7,9,12,4,5,9,1,2,3,2,1]
n = len(A)
for i in range(n):
    for j in range(0,n-i-1):
        if A[j] > A[j + 1]:
            A[j],A[j + 1] = A[j+1],A[j]
print(A)

