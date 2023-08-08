# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        res = list()
        for x in lists:
            while x:
                res.append(x.val)
                x = x.next
        out = ListNode(0)
        head = out
        for x in sorted(res):
            head.next = ListNode(x)
            head = head.next
        return out.next