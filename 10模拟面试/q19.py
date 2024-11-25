'''
题目：集合2

题意：
 Problem Statement: Given an integer array nums that may contain duplicates, return all possible subsets (the power set). The solution set must not contain duplicate subsets, and the result can be returned in any order.

 思路：
 algorithm used: dfs and backtrack
 We use a backtracking approach to generate all possible subsets while avoiding duplicates.

 steps:
 1. Sort the array nums to ensure duplicates are adjacent, which makes it easier to skip them.
 2. Use a recursive backtracking function to generate subsets. For each recursive call, add the current path to the result.'
 3. To avoid duplicate subsets, skip over duplicates in the array. For each position, only add the current element if it’s the first of its kind in that position of the recursion (i.e., skip it if it’s the same as the previous element).
 4. Collect all unique subsets in the result array.
 '''

def solution(nums:list[int])->list[list[int]]:
    res = []
    def backtrack(start, path):
        # Append a copy of the current path as a subset
        res.append(path[:])
        # Generate subsets from the current element onward
        for i in range(start, len(nums)):
            # Skip duplicates
            if i > start and nums[i] == nums[i - 1]:
                continue
            # Include the current element and continue
            path.append(nums[i])
            backtrack(i + 1, path)
            # Backtrack by removing the current element
            path.pop()
     # Initialize result array and sort input to handle duplicates
    nums.sort()
    backtrack(0, [])
    return res

'''
Time Complexity: O(2^n), where n is the length of the array nums. Each element has two states: either included in the subset or not, leading to 2^n possible subsets. 

Space Complexity: O(n), because the recursion depth can go up to n,We will take up space on the recursion stack
'''