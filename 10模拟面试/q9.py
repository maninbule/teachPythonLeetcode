'''
题意：
Given a linked list, delete the nth last node of the linked list.
input: The first node of the linked list
output: The first node after processing the above operations


思路：
steps:
1. First, we can determine the length of this linked list.
2. After determining the length, we can know the position of the nth last node
3. For example, if the total length is len, then the nth to last number is the len - n + 1th number from the beginning.
4. After that, we can create a new linked list and traverse the original linked list, skip the nodes that need to be deleted, keep the nodes that do not need to be deleted, and insert them into the new linked list.
5. Returns the new linked list


'''

# 代码

# Define the node class of the linked list
class Node:
    def __init__(self,val:int) -> None:
        self.val = val
        self.next = None

def solution(head:Node,n:int)->Node:
    # First, we determine the length of the linked list.
    length = 0
    curNode = head
    while curNode:
        #If the current node is not empty, the length is increased by 1.
        length += 1
        curNode = curNode.next # Move to the next node
    k = length - n + 1 # Turn the nth one from the right into the kth one from the left
    dummy = Node() # Define a virtual head node to facilitate the insertion of new elements
    tail = dummy
    curNode = head
    for i in range(1,length + 1):
        if i == k:# Skip the nodes that need to be deleted
            curNode = curNode.next
            continue
        else:
            tail.next = curNode #Insert the new node at the end of the new linked list
            curNode =curNode.next
            tail = tail.next
    tail.next = None
    return dummy.next

'''
Time complexity: O(n) Each node only needs to be visited twice, once when calculating the length of the linked list, and once when traversing the linked list when performing a deletion operation
Space complexity: O(1) No array is allocated
'''