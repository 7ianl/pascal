# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        out = ListNode(0, head)
        res = out.next
        if res == None:
            return res
        while res and res.next:
            if res.next.val == res.val:
                res.next = res.next.next
            else:
                res = res.next
        return out.next
        