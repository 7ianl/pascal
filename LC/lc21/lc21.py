# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        output = ListNode()
        acc = output
        while l1 and l2:
            if l1.val < l2.val:
                acc.next = ListNode(l1.val)
                l1 = l1.next
                acc = acc.next
            else:
                acc.next = ListNode(l2.val)
                l2 = l2.next
                acc = acc.next
        if l1:
            acc.next = l1
        else:
            acc.next = l2
        return output.next