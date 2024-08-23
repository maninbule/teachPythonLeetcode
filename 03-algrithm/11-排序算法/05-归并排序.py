'''
时间复杂度: O(nlogn)
空间复杂度: O(n)
'''

def sort(arr:list[int])->list[int]:
    merge_sort(arr,0,len(arr)-1)
    return arr
def merge_sort(arr:list[int],left:int,right:int):
    # 如果最多只有一个元素了，那么肯定就是已经有序了，直接返回
    if right - left + 1 <= 1:
        return
    # 还未排序，目前arr[left：rihgt]的长度大于等于2，需要对半分
    mid = (left + right)//2
    merge_sort(arr,left,mid)
    merge_sort(arr,mid + 1,right)
    # 此时，区间[left,mid], 以及[mid+1,right]就分别有序了
    # 现在就要进行合并
    tmp = [0] * len(arr)
    p1,p2 = left,mid + 1
    for i in range(left,right + 1):
        if p1 <= mid and p2 <= right:
            if arr[p1] <= arr[p2]:
                tmp[i] = arr[p1]
                p1 += 1
            else:
                tmp[i] = arr[p2]
                p2 += 1
        elif p1 <= mid:
            tmp[i] = arr[p1]
            p1 += 1
        else:
            tmp[i] = arr[p2]
            p2 += 1
    for i in range(left,right + 1):
        arr[i] = tmp[i]

A = [1,2,3,6,7,9,12,4,5,9,1,2,3,2,1]
A = sort(A)
print(A)
