# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        itemlist = []
        while head:
            itemlist.append(head.val)
            head = head.next
        itemlist.pop(-n)
        output = None
        while itemlist:
            output = ListNode (itemlist[-1], output)
            itemlist.pop(-1)
        return output