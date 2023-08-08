# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        mem = []
        while head:
            mem.append(head.val)
            head = head.next
        return mem == mem[::-1]