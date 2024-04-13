


arr = [1,3,2,4,5]
arr_with_index = []
for i in range(len(arr)):
    arr_with_index.append([arr[i],i])
arr_with_index.sort(key=lambda x:x[0])
ans = [0] * len(arr)
for i in range(len(arr)):
    ans[arr_with_index[i][1]] = len(arr) - i - 1
print(ans)

