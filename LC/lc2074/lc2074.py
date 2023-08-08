# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseEvenLengthGroups(self, head: Optional[ListNode]) -> Optional[ListNode]:
        res = ListNode()
        out = res
        def helper(head, res, remaining):
            if not head or remaining == 0:
                return res
            res = ListNode(head.val, res)
            return helper(head.next, res, remaining-1)
        
        group = 0
        while head:
            group += 1
            tmp = group
            
            test, l = head, 0
            
            while test != None and l < group:
                test = test.next
                l+= 1
                
            if l % 2:
                while group and head:
                    res.next = ListNode(head.val)
                    res = res.next
                    head = head.next
                    group -= 1
            else:
                acc = helper(head, None, group)
                while group and head:
                    res.next = ListNode(acc.val)
                    acc = acc.next
                    head = head.next
                    res = res.next
                    group -= 1
            group = tmp
        return out.next