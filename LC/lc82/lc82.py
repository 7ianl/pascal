# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        out = ListNode(-10000, head)
        vals = set()
        res = out.next
        while res and res.next:
            if res.val == res.next.val:
                vals.add(res.val)
            res = res.next
        res = out
        while res.next:
            if res.next.val in vals:
                res.next = res.next.next
            else:
                res = res.next
        return out.next
                
        