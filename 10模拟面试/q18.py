
'''
题意：
Rearrange to ensure that two adjacent characters are different

思路：
Algorithm: greedy and priority queue
steps:
1. We will use the greedy strategy
2. First initialize an empty string to store the results.
3. put the characters with the highest frequency among the remaining characters.
4. Take out the two most frequent two different characters each time, select a character that is different from the last character of the result string, and put it in

For example, the current result string is aba. Among the remaining strings, the two most frequent ones are a and c. The frequency of a is higher than c.
But since the last character of the result string is a, c is currently put in

5. To count the frequency of letters, we can use a hash table to calculate
6. In order to quickly remove the characters with the highest frequency in the remaining strings, you can use the priority queue to process


'''
# 代码
# Import priority queue
from queue import PriorityQueue
def solution(s :str )- >str:
    # Define a hash table to count the number of occurrences of each character
    char_count = {}
    for c in s:
        if c in char_count:
            char_count[c] += 1
        else:
            char_count[c] = 1
    max_heap = PriorityQueue()
    # Add each character and its frequency to the priority queue (the frequency takes a negative value to achieve from high to low frequency)
    for char, freq in char_count.items():
        max_heap.put((-freq, char))
    result = [] # We use a list to store characters, and finally turn them into strings, which is more efficient.


    while max_heap.qsize() >= 2: # When there are 2 different characters in the priority queue, execute the loop
        # Take out the two characters with the highest frequency
        freq1, char1 = max_heap.get()
        freq2, char2 = max_heap.get()
        if result == [] or char1 != result[-1]:
            # When it has not been saved before, you can put both char1 and char2.
            result.append(char1)
            freq1 += 1 # Reduce the frequency by 1 and use the +1 operation, because the negative numbers previously stored are only in max_heap
            if freq1 != 0:
                max_heap.put((freq1, char1))
        else:
            result.append(char2)
            freq2 += 1
            if freq2 != 0:
                max_heap.put((freq2, char2))
    # Now, there is only one character
    # But you may encounter 2 unsolvable situations
    # In the end, there is only one kind of character left. If the last remaining character is the same as the last character in the result string, there is no solution.
    # Or the number of the last character is greater than or equal to 2, which is also unsolvable
    if len(s) == 0: # Only this edge case requires additional processing, empty input
        return ""
    # Because we are putting characters one by one into the resulting string,
    # There must be one character left in the end
    freq1, char1 = max_heap.get()
    if len(result) > 0 and char1 == result[-1]:
        return None
    if freq1 > 1  :# Because this kind of characters will definitely be adjacent, which also means that they appear the most in strings.
        return None
    result.append(char1)
    return "".join(result) # Concatenate strings into strings and return the answer

'''
example:
example:
input: bcaaa
max_heap = {a:3,b:1,c:1}
Take out a:3,b:1
result = a

max_heap = {a:2,b:1,c:1}
Take out a:2,b:1
result=ab

max_heap = {a:2,c:1}
Take out a:2,c:1
result=aba

max_heap = {a:1,c:1}
Take out a:1,c:1
result=abac

max_heap = {a:1}
There is only one character
Take out a:1
result=abaca

so,ouput is abaca



time: O(nlogn) edge case, all characters have different frequencies, all letters will enter the priority queue
The put and get of the priority queue are both logn
space: O(n) Because the priority queue is used to store elements
'''

