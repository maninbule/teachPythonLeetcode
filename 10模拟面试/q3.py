'''
题意：
The task is to group strings that are anagrams. Anagrams are words that can be formed by rearranging the letters of another word. For example, "eat" and "tea" are anagrams because their characters can be rearranged to form each other.
Given an array of strings, we need to return a list of lists where each sublist contains words that are anagrams of each other. The order of the anagrams in the sublists, or the order of the sublists themselves, does not matter.
high-level idea:
1. Algorithm and Data Structures:
We will use hash table to solve this problem.
Data structure: Dictionary (dict)
Algorithm: Sorting the characters of each string to determine if two strings are anagrams.
2. Why Use This Algorithm and Data Structure:
Dictionary: It allows us to map each sorted string (as the key) to a list of anagrams (as the value). It efficiently groups strings that have the same sorted character order.

Sorting: Sorting the characters in a string gives a canonical form that helps easily identify anagrams, as all anagrams will have the same sorted character order.

3. Step-by-Step Approach:
High-Level Idea:
The core idea is to:

Sort each string’s characters.
Use the sorted string as a key in a dictionary.
Append the original string to the list corresponding to the sorted string.
Finally, return the values of the dictionary.

例子：
举例的题目的例子
strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
For "eat", sorted is "aet". Add "eat" to the dictionary under key "aet".
hash table = {
    "aet": ["eat"],
}
For "tea", sorted is "aet". Add "tea" to the list under the key "aet".
hash table = {
    "aet": ["eat","tea"],
}
For "tan", sorted is "ant". Add "tan" to the dictionary under key "ant".
hash table = {
    "aet": ["eat","tea"],
    "ant": ["tan"]
}
For "ate", sorted is "aet". Add "ate" to the list under the key "aet".
hash table = {
    "aet": ["eat","tea","ate"],
    "ant": ["tan"]
}
For "nat", sorted is "ant". Add "nat" to the list under the key "ant".
hash table = {
    "aet": ["eat","tea","ate"],
    "ant": ["tan","nat"]
}
For "bat", sorted is "abt". Add "bat" to the dictionary under key "abt".
so hash table = {
    "aet": ["eat","tea","ate"],
    "ant: ["tan","nat"]
    "abt":["bat"]
}

so return all list in dict:  [["bat"],["nat","tan"],["ate","eat","tea"]]

Time Complexity:  O(nklogk)
Sorting each string takes
O(klogk), where k is the length of the string. If there are n strings, the total time complexity is O(n⋅klogk).

Space Complexity:O(nk)
We use a dictionary to store the all strings
where n is the number of strings
k is the average length of the strings.

'''

from collections import defaultdict


def groupAnagrams(strs):
    # Create a dictionary to store lists of anagrams
    anagrams = defaultdict(list)

    # Iterate through each string in the input list
    for s in strs:
        # Sort the characters in the string and use it as the key
        sorted_s = ''.join(sorted(s))
        # Append the original string to the list corresponding to the sorted key
        anagrams[sorted_s].append(s)

    # Return all values from the dictionary, which are the lists of anagrams
    return list(anagrams.values())


# Example test case
strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
print(groupAnagrams(strs))
