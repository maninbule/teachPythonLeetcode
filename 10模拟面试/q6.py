'''
题意：
Given an array, you can select any number from this array. We need to output all selections.

思路：
Algorithm used: Recursive
steps:
1. We can use recursion to select numbers. The i-th level of recursion is to consider the i-th element of the array, whether to choose or not to choose.
2. Each level of recursion will make a choice or not, and then go to the next level of recursion to consider whether to choose the next number or not.
3. When we have considered all the numbers in the array, we put the currently selected number into the answer array.
4. We need to use a common choose array. When a number is selected, it is added to this array. If the selection is deselected, the number is deleted from the choose array.

We can make an explanation of the example given in the question
Input: nums = [1,2,3]
Output: [[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]]
The case of selection can be represented by a binary tree, where a node going to its left node is selecting the current number, and going to its right child is not selecting the current number

for 1                                []

for 2         (choose 1) 1                not choose []


for 3    [1,2]      [1]                    [2]       []

[1,2,3]   [1,2]  [1,3]  [1]         [2,3]   [2]    [3]   []

That is, all the leaf nodes of this binary tree are all the selection situations.


'''

# 代码

class Solution:
    # Define a helper function to complete the recursive selection of the numbers in the nums array.
    def dfs(self,nums:list[int],i:int,choose:list[int]):
        #
        if i >= len(nums):# If all the numbers have been considered, take the current selection situation and add it to the answer array
            self.result.append([x for x in choose])
            return
        # choose nums[i]
        choose.append(nums[i])
        self.dfs(nums,i + 1,choose)
        choose.pop() # delete the number you just selected here, because the next step is to not select the current number.
        # not choose nums[i]
        self.dfs(nums,i + 1,choose)
    def subsets(self, nums: list[int]) -> list[list[int]]:
        choose = [] # Store the current selection
        self.result = [] # Store final answer
        self.dfs(nums,0,choose) # start recursion
        return self.result

'''
The time complexity is: O(2^n) Because each number has two situations: choice and no choice. There are n numbers in total, so there are 2^n answers in total.
Space complexity: O(n) because at most n elements are selected
'''