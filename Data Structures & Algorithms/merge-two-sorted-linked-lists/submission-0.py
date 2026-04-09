# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        ptr1 = list1
        ptr2 = list2
        head = ListNode()
        curr = head
        if not ptr1 and not ptr2:
            return None

        while ptr1 or ptr2:
            if not ptr1:
                curr.next = ptr2
                break
            if not ptr2:
                curr.next = ptr1
                break
            if ptr1.val < ptr2.val:
                curr.next = ptr1
                ptr1 = ptr1.next
            else:
                curr.next = ptr2
                ptr2 = ptr2.next
            curr = curr.next
        return head.next
