'''
Problem Explanation:
    The encoded string follows the format k[encoded_string], where k is a positive integer representing the number of times the string inside the square brackets encoded_string should be repeated.

For example:
    Input: "3[a]2[bc]"
    First, the inner string bc is repeated 2 times to become bcbc.
    Then, the entire result a + bcbc is repeated 3 times, yielding the final output "aaabcbc".

    3[a] = "aaa"
    2[bc] = "bcbc"
    so 3[a]2[bc] = "aaabcbc"

思路：
关键词：  Depth-First Search (DFS) , stack
use a Depth-First Search (DFS) approach to recursively decode the string. The key idea is to match the pairs of brackets first, so we know which part of the string to decode recursively. The main function decodeString first builds the matching brackets and then calls the recursive dfs function to construct the decoded string.

Time Complexity: O(n), where n is the length of the input string. Each character is processed exactly once, and the recursive calls handle nested brackets.

Space Complexity: O(n), where n is the size of the output string.

'''


class Solution:
    def decodeString(self, s: str) -> str:
        # Initialize the result and the match array to store corresponding brackets
        res = ""
        match = [0] * len(s)  # Stores positions of matching brackets
        sk = []  # Stack to keep track of left bracket indices

        # First, find matching brackets and store them in the match array
        for i in range(len(s)):
            if s[i] == '[':
                sk.append(i)  # Push index of '[' onto the stack
            elif s[i] == ']':
                left = sk.pop()  # Pop the matching '[' index
                match[left] = i  # Store the matching position in the match array

        # Call the dfs function to decode the string from start to end
        return self.dfs(s, 0, len(s) - 1, match)

    def dfs(self, s: str, left: int, right: int, match: list[int]) -> str:
        res = ""  # This will store the decoded result
        curNumber = 0  # To keep track of the current number (repetition count)
        i = left  # Start index for the current substring

        # Loop through the string from 'left' to 'right'
        while i <= right:
            c = s[i]
            if c.isdigit():
                # Build the number (account for multiple digits)
                curNumber = curNumber * 10 + int(c)
                i += 1
            elif c == '[':
                # Find the corresponding ']' using the match array
                right_index = match[i]

                # Recursively decode the substring inside the brackets
                # Multiply the decoded result by the current number
                res += curNumber * self.dfs(s, i + 1, right_index - 1, match)

                # Reset curNumber and move i past the closing bracket
                curNumber = 0
                i = right_index + 1
            else:
                # If it's a regular character, add it to the result
                res += c
                i += 1

        return res  # Return the decoded string


solution = Solution()

# Test cases
print(solution.decodeString("3[a]2[bc]]"))  # Expected output: "aaabcbc"
print(solution.decodeString("2[abc]3[cd]ef"))  # Expected output: "abcabccdcdcdef"
print(solution.decodeString("3[a2[c]]"))  # Expected output: "accaccacc"
print(solution.decodeString("10[a]"))  # Expected output: "aaaaaaaaaa"
print(solution.decodeString("2[ab3[c]]"))  # Expected output: "abcccabccc"