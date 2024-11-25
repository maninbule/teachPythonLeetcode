'''
Given a string s, find the length of the longest
substring
 without repeating characters.

Example 1:
Input: s = "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3.

Example 2:
Input: s = "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.

Example 3:
Input: s = "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3.
Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.



def  solution(s:str)->int:
	seen_chars = set()
	left = 0
	max_length = 0
	for right in range(len(s)):
		while s[right] in seen_chars:
			seen_chars.remove(s[left])
			left += 1
		seen_chars.add(s[right])
		max_length = max(max_length,right-left+1)
	return max_length


time:O(n)
space: O(min(m,n))

'''



'''
题意：
Given a string s, find the length of the longest substring without repeating characters.

思路：
Algorithm used: two pointer
steps:
1. Initialize two pointers, left and right, both starting at the beginning of the string, representing the boundaries of the window.
2. Use a set seen_chars to store characters currently within the window.
3. Iterate over each character with the right pointer:
    If s[right] is not in seen_chars, add it to the set, and update the maximum window length.
    If s[right] is already in seen_chars, increment the left pointer to reduce the window size until the duplicate character is removed.
4. Return the maximum recorded window length as the result.

'''

def solution(s:str)->int:
    seen_chars = set() # Store characters in the current window
    left = 0 # Left boundary of the window
    max_length = 0 # Track the maximum window size
    for right in range(len(s)):
        # If a duplicate character is found, shrink the window by moving the left pointer
        while s[right] in seen_chars:
            seen_chars.remove(s[left])
            left += 1
        # Add the current character to the set
        seen_chars.add(s[right])
        # Update the maximum window size
        max_length = max(max_length, right - left + 1)
    return max_length

'''
Time Complexity: O(n), where n is the length of the string. Each character is processed by both left and right pointers only once. 
Space Complexity: O(min(m, n)), where m is the character set size (assuming a constant ASCII set size of 256). This is for storing characters in the set. 
'''