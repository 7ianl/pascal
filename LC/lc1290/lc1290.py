# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def getDecimalValue(self, head: ListNode) -> int:
        stack = []
        while head:
            stack.append(str(head.val))
            head = head.next
        return int(''.join(stack), 2)