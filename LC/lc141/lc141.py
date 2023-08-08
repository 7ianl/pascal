# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        while True:
            if head == None:
                return False
            if head.val == 'a':
                return True
            head.val = 'a'
            head = head.next