'''
给你一个元素递增的数组:
arr = [-1,0,1,1,1,2,2,3,4,4,4,4,4,7,7,7,8]
求解相同数字连续的最大个数
输出：5
'''

# 二分优化，可以优化这样的数据，有大量元素连续重复出现
# 时间复杂度: O(klogn) k是不同元素的个数
# 空间复杂度: O(1)
def solution(arr:list[int])->int:
    if arr == []:
        return 0
    res = 0
    i = 0
    while i < len(arr):
        if i + 1 < len(arr) and arr[i + 1] != arr[i]:
            res = max(res,1)
            i = i + 1
            continue
        left,right = i,len(arr)-1
        lastPost = -1
        while left <= right:
            mid = (left + right)//2
            if arr[mid] == arr[i]:
                lastPost = mid
                left = mid + 1
            else:
                right = mid - 1
        res = max(res,lastPost - i + 1)
        i = lastPost + 1
    return res

print(solution([-1,0,1,1,1,2,2,3,4,4,4,4,4,7,7,7,8]))
print(solution([-1]))
print(solution([]))
print(solution([1,1,1,1,1]))
print(solution([1,2,5,6,7,8]))

