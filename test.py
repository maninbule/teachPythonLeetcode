
arr = [1 ,2 ,3 ,2 ,3 ,5 ,7]
k = 5
ans = set()
for i in range(len(arr)):
    for j in range(len(arr)):
        if i == j :continue
        if arr[i] + arr[j] == k:
            ans.add((arr[i] ,arr[j]))
print(len(ans))