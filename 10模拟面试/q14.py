'''
题意：
Given a string, you need to merge adjacent identical characters. The merging format is: character + number of times. If the number of times is 1, you can omit it.
We need to output the length of the string after processing

思路：
Algorithm used: Two pointers
1. Initialize a pointer i to the start of the character array to track the insertion position for the compressed characters.
2. Use another pointer j to iterate through the character array, counting occurrences of the current character.
3. When a different character is encountered, add the current character and its count to the array and update pointer i.
4. Return the new length of the modified array.


'''


# 代码
def solution(chars: list) -> int:
    n = len(chars)  # Get the length of the input array
    if n == 0: return 0

    i = 0  # Pointer for the insertion position in the new array
    j = 0  # Pointer for traversing the input array

    while j < n:
        current_char = chars[j]
        count = 0  # Count occurrences of the current character

        while j < n and chars[j] == current_char:
            count += 1
            j += 1
        # Add the current character to the array
        chars[i] = current_char
        i += 1
        # If the count is greater than 1, convert the count to characters and add to the array
        if count > 1:
            for digit in str(count):
                chars[i] = digit
                i += 1
    return i


'''
Time Complexity: O(n), where n is the length of the character array. Each character is accessed at most twice. 
Space Complexity: O(1), as only constant extra space is used without any additional data structures.
'''