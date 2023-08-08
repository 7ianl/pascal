# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        res = ListNode(0, ListNode(0))
        head = res.next
        carry = 0
        while l1 and l2:
            numrep = l1.val + l2.val + carry
            if numrep <= 9:
                carry = 0
                head.next = ListNode(numrep)
            else:
                carry = 1
                head.next = ListNode(numrep - 10)
            l1 = l1.next
            l2 = l2.next
            head = head.next
        while l1:
            numrep = l1.val + carry
            if numrep <= 9:
                carry = 0
                head.next = ListNode(numrep)
            else:
                carry = 1
                head.next = ListNode(numrep - 10)
            l1 = l1.next
            head = head.next
        while l2:
            numrep = l2.val + carry
            if numrep <= 9:
                carry = 0
                head.next = ListNode(numrep)
            else:
                carry = 1
                head.next = ListNode(numrep - 10)
            l2 = l2.next
            head = head.next
        if carry:
            head.next = ListNode(carry)
        return res.next.next