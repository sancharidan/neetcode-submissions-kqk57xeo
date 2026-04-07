# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        minheap = []
        dummy = ListNode()
        curr = dummy
        for i, node in enumerate(lists):
            if node:
                heapq.heappush(minheap, (node.val, i, node))

        while minheap:
            val, i, node = heapq.heappop(minheap)
            curr.next = node
            curr = node
            node = node.next
            if node:
                heapq.heappush(minheap, (node.val, i, node))
        
        return dummy.next