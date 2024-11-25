'''
题意：
The meaning of the question is that we add a function to randomly obtain elements based on the ordinary hash table, which requires a time complexity of O(1)

思路：
algorithm used: Hash Map and Array
To achieve average O(1) time complexity for each operation, we will use a combination of a hash map and an array:
Insert Operation:
    Use a hash map to store the element as the key and its index in the array as the value.
    Insert the element into the array if it doesn't already exist in the set (check using the hash map).
Remove Operation:
    To remove an element efficiently, we swap it with the last element in the array, then remove the last element. This allows us to maintain the array's integrity without shifting all other elements.
GetRandom Operation:
    Simply return a random index from the array. Since the array has no gaps and the elements are contiguous, retrieving a random element is an O(1) operation.
'''

# 代码
import random

class RandomizedSet:
    def __init__(self):
        # Initialize the set with a hash map and an array
        self.val_map = {}  # Hash map to store element to index mapping
        self.val_list = []  # Array to store elements

    def insert(self, val: int) -> bool:
        if val in self.val_map:
            return False  # Element already exists
        # Add the value to the list and map it to its index
        self.val_map[val] = len(self.val_list)
        self.val_list.append(val)
        return True

    def remove(self, val: int) -> bool:
        if val not in self.val_map:
            return False  # Element doesn't exist
        # Get the index of the element to be removed
        index = self.val_map[val]
        # Swap the element with the last element in the array
        last_val = self.val_list[-1]
        self.val_list[index] = last_val
        self.val_map[last_val] = index
        # Remove the last element
        self.val_list.pop()
        del self.val_map[val]
        return True

    def getRandom(self) -> int:
        # Return a random element from the list
        return random.choice(self.val_list)
'''
时间复杂度：

Insert: O(1), checking the existence of an element and appending to the array both take constant time.
Remove: O(1), removing an element involves swapping it with the last element and then removing it from the array.
GetRandom: O(1), accessing a random element from the array is a constant-time operation.
空间复杂度：

O(n), where n is the number of elements in the set. We store the elements in both the hash map and the array, so the space complexity is proportional to the number of elements.
'''