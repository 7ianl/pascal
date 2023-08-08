# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        vals = []
        while head:
            vals.append(head.val)
            head = head.next
        for i in range(len(vals)//k):
            vals[i*k:(i+1)*k] = reversed(vals[i*k:(i+1)*k])
        res = ListNode()
        head = res
        for x in vals:
            head.next = ListNode(x)
            head = head.next
        return res.next