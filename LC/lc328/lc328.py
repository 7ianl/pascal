# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        acc = ListNode()
        res = ListNode(0, acc)
        counter = 0
        evens = ListNode()
        e1 = ListNode(0, evens)
        if not head: return None
        if not head.next: return head
        while head:
            counter += 1
            if counter%2:
                acc.val = head.val
                if head.next and head.next.next:
                    acc.next = ListNode()
                    acc = acc.next
                head = head.next
            else:
                evens.val = head.val
                if head.next and head.next.next:
                    evens.next = ListNode()
                    evens = evens.next
                head = head.next
        acc.next = e1.next
        return res.next