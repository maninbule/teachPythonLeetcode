'''
题意:
Problem Statement: Given an array of k sorted linked-lists, each linked-list is sorted in ascending order. Merge all the linked-lists into one sorted linked-list and return it.

思路：
algorithm used: priority queue
We use a priority queue to efficiently merge multiple sorted linked lists. This approach ensures that the smallest element is always at the top of the heap, allowing us to extract the elements in sorted order.

steps:
1. Initialize a priority queue (min-heap). We will insert the first node of each linked list into the heap.
2. While the heap is not empty, extract the smallest element from the heap and add it to the result list.
3. If the extracted element has a next node, push the next node into the heap.
4. Continue this process until all nodes from all linked lists are processed.
5. Return the merged sorted linked list.
'''

# 代码
import heapq


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def mergeKLists(lists: list[ListNode]) -> ListNode:
    # Define the priority queue (min-heap)
    min_heap = []
    # Push the first node of each list into the heap
    for i, cur_list in enumerate(lists):
        if cur_list:
            heapq.heappush(min_heap, (cur_list.val, i, cur_list))
    # Dummy node to simplify the merging process
    dummy = ListNode()
    current = dummy

    # Process the heap
    while min_heap:
        # Extract the smallest node from the heap
        val, idx, node = heapq.heappop(min_heap)
        current.next = node
        current = current.next

        # If the node has a next, push it into the heap
        if node.next:
            heapq.heappush(min_heap, (node.next.val, idx, node.next))

    # Return the merged linked list
    return dummy.next


'''
Time complexity:
O(N * log K), where N is the total number of nodes in all linked lists and K is the number of linked lists. Each extraction of the smallest element from the heap takes O(log K) time, and a total of N elements are extracted.

Space complexity:
O(K), since there will be at most K elements in the heap, the space complexity is O(K), where K is the number of linked lists.
'''