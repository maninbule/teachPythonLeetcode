



def solve(arr:list[int])->int:
    st = set()
    for i in range(len(arr)):
        for j in range(len(arr)):
            for k in range(len(arr)):
                if i != j and j != k and i != k:
                    if arr[i] + arr[j] == arr[k]:
                        st.add((arr[i],arr[j],arr[k]))
    return len(st)

# 测试
arr = [2,2,2,1,3,4]
print(solve(arr)) # 5  (2,2,4),(1,3,4),(3,1,4),(1,2,3),(2,1,3)

