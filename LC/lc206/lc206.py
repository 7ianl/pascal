# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        def rev_aux (head, res):
            if head:
                res = ListNode(head.val, res)
                return rev_aux(head.next, res)
            return res
        return rev_aux(head, None)
        