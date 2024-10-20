'''

Problem:
Given an array of integers, all elements appear twice except for one element that appears exactly once. You need to find and return the element that appears only once. Use a hash table for this solution.


Example Explanation:
    Let's say the input array is [4, 1, 2, 1, 2].

    First, we traverse through the array and build the frequency dictionary:

    {4: 1, 1: 2, 2: 2}
    Next, we iterate through the dictionary:

    4 has a count of 1, so we return 4.
    Thus, the output will be 4.

Approach:
The idea is to use a hash table (or dictionary in Python) to store the frequency of each element in the array. Once we've populated the hash table, we can iterate through it to find the element that has a count of 1.

Steps:
Initialize an empty hash table (frequency dictionary).
Traverse through the array and for each element:
If it is already in the hash table, increment its value (count).
If it is not in the hash table, add it with a count of 1.
After populating the hash table, iterate through the dictionary to find the key (element) with a value of 1.
Return that element.


Time Complexity:
O(n): where n is the number of elements in the array. We traverse the array once to build the frequency dictionary and then iterate through the dictionary once, making it linear.
Space Complexity:
O(n): We use a hash table (dictionary) to store the frequency of each element, which in the worst case could store all elements.
'''


def find_single_number(nums):
    frequency = {}

    # Build frequency dictionary
    for num in nums:
        if num in frequency:
            frequency[num] += 1
        else:
            frequency[num] = 1

    # Find and return the element that appears once
    for num in frequency:
        if frequency[num] == 1:
            return num


'''
edge cases:
input = [] return None
input = [2,3,3,4,4] return 2
'''