'''
题意：
Given an array, we select some numbers from this array. These numbers are consecutive. We want to select the one with the largest number of consecutive elements. We only need to output the number of elements.
思路：
Algorithm used: Hash table
steps:
1. It can be found that this array can actually be divided into segments composed of several consecutive numbers.
2. [100,4,200,1,3,2] can split to [1,2,3,4], [100] ,[200]
3. We can use the minimum value of each segment as a starting point, continuously add 1, and determine whether it is still stored in the hash table after adding 1.
4. Then you can use this method to know how far each number can go if it is used as the starting point of a continuous number.
5. The starting point can be judged as follows: If the current number x is the starting point, then x-1 definitely does not exist in the hash table.

'''
# 代码

def solution(arr:list[int])->int:
    # The input is an array and the output is a number
    hash_table = {}
    for x in arr:
        hash_table[x] = True
    max_length = 0
    for x in arr:
        if x - 1 not in hash_table:
            #find a starting point
            cur_length = 0
            # Continuously add 1 from the starting point to determine whether it is in the hash table
            while x in hash_table:
                cur_length += 1
                x += 1
            max_length = max(max_length,cur_length) # Update maximum value
    return max_length

'''
Time complexity: O(n) because you only need to put the traversed elements into the hash table, and then traverse all elements. Each element will only be traversed twice.
Space complexity: O(n) because n elements need to be put into the hash table
'''