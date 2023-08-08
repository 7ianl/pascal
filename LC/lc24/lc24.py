# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        if not head or not head.next:
            return head
        else:
            t = self.swapPairs(head.next.next)
            r = head.next
            r.next = head
            head.next = t
            return r