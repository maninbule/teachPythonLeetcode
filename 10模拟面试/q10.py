'''
题目：
The requirement of the question is to divide an array into k groups, each group has at least 1 element, and then sum up each group to find the maximum sum. We require this sum to be the smallest and output this sum

例如：
[7,2,5,10,8], k = 2
Output: 18
After being divided into 2 groups, the two groups are [7,2,5],[10,8] and the sums of the two groups are 14 and 18 respectively.
If we divide it into [7,2],[5,10,8], the maximum sum is 23
So it can only be divided into [7,2,5], [10,8], and the largest group, the sum is 18

思路：
Algorithm used: binary search
steps:
1. Determine the range of bisection, the minimum value is max(arr), the maximum value is sum(arr)
2. Define a check function, which can limit a capacity to each group and see how many groups are needed to allocate all elements to each group if each group does not exceed this capacity.
3. We define the capacity of the group as cap. If it is within the capacity limit of cap, a total of x groups are needed to allocate all elements.
4. If x is greater than k, it means that our capacity is set too small. If the capacity is too small, more groups will be needed. We need to adjust the capacity to be larger.
5. If x is less than or equal to k, record the capacity, adjust the capacity to be smaller, and try to find a smaller answer

'''

# 代码
class Solution:
    def splitArray(self, arr: list[int], k: int) -> int:
        if len(arr)  < k:
            return None # If the number of elements in the array is less than k, it will definitely not be divided into k groups, and None will be returned to indicate that there is no solution.
        def check(cap:int)->bool:
            # Check how many groups each group is divided into at least according to the capacity of cap.
            # If the divided groups are less than or equal to k, then if divided into k groups, it must also be true, and return true
            # If the group it is divided into is greater than k, then return false
            cnt = 0 # Record the number of groups required
            cur = 0 # sum of current group
            for x in arr:
                if cur + x <= cap: # The current x can be placed in the previous group
                    cur += x
                else:# If the current x is placed in the previous group, the capacity will be exceeded, so add 1 to the number of groups, and then open a new group.
                    cnt += 1
                    cur = x
            cnt += 1
            if cnt <= k: # The number of groups is less than or equal to k, indicating that it satisfies
                return True
            else:
                return False
        # Determine the range of the two points
        left,right = max(arr) ,sum(arr)
        res = 0
        while left <= right:
            mid = (left + right)//2
            if check(mid): # Can be divided into k groups under the condition of mid capacity
                res = mid
                right = mid - 1
            else:
                left = mid + 1
        return res

'''
Time complexity: O(nlogsum(arr)) The time complexity of bisection is logsum(arr). Each bisection requires traversing the array, which requires O(n) complexity, so the overall time complexity is O(nlogsum(arr) ))
Space complexity: O(1) without opening up additional array space

对example 进行dry-run:

arr = [7,2,5,10,8], k = 2
1. 
left = max(arr) = 10
right = sum(arr) = 32
mid = (left + right)//2 = 21
res = 0
check(cap = 21):
arr split to [7,2,5],[10,8]
res = 21

2. left= 10,right = 20,mid = 15
check(cap = 15):
arr split to [7,2,5],[10],[8]
When the capacity is 15, 3 groups are needed, so it is not satisfied and the group capacity needs to be increased.
res = 21

3. left =  16, right = 20,mid = 18
check(cap = 18):
arr split to [7,2,5],[10,8]
res = 18

4. left = 16,right = 17,mid = 16
check(cap = 16):
arr split to [7,2,5],[10],[8]
When the capacity is 16, 3 groups are needed, so it is not satisfied and the group capacity needs to be increased.

5. left = 17,right = 17,mid = 17
check(cap = 17):
arr split to [7,2,5],[10],[8]
When the capacity is 17, 3 groups are needed, so it is not satisfied and the group capacity needs to be increased.
6. left = 18,right = 17

If left <= right is not satisfied, the binary search needs to finish

so result = 18
'''