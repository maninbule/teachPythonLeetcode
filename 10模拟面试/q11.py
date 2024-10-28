'''
题意：
Given an array, we need to select some numbers from this array, but we can only select numbers from both ends of the array. What is the maximum sum of the selected k numbers?

思路：
1. Since k numbers are fixed, if x numbers are selected on the left, then only k-x numbers can be selected on the right.
2. There are k+1 ways to choose on the left: none, 1, 2, ... choose k elements
3. So there are k + 1 cases in total, so we can use enumeration to handle all cases
4. In addition, we have selected x on the left and k-x on the right. We need to quickly query the sum of the k-x elements on the right. We can use prefix sum to optimize the time complexity of the query.
'''


def solution(arr: list[int], k: int) -> int:
    if len(arr) < k:
        # If the number of elements in the array is less than k, there is definitely no solution.
        return None
    suf_sum = [0] * len(arr)
    for j in range(len(arr) - 1, -1, -1):  # Traverse backwards
        suf_sum[j] = arr[j]
        if j + 1 < len(arr):
            suf_sum[j] += suf_sum[j + 1]
    # suf_sum[j]: suf_sum[j]: represents the sum of the elements after index j
    res = 0  # Record the answer
    left_sum = 0  # Record the sum of the numbers selected on the left
    for i in range(len(arr)):
        left_sum += arr[i]  # Update the sum of the numbers selected on the left
        if i + 1 > k:  # If the number selected on the left exceeds k, exit the loop
            break
        right_cnt = k - i  # Calculate how many elements can be selected on the right
        right_sum = suf_sum[len(arr) - right_cnt + 1]  # Calculate the sum of the numbers selected on the right
        res = max(res, left_sum + right_sum)  # Update final answer
    return res


'''
Time complexity: O(n) because at most n elements are traversed
Space complexity: O(n) because we open up a new array, the length of this array is n
'''
