# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def nodesBetweenCriticalPoints(self, head: Optional[ListNode]) -> List[int]:
        prev = head.val
        n = head.next
        p, points, f = 0, [], 0
        while n:
            if n.val > prev:
                if f == 1:
                    points.append(p)
                f = 2
                p+= 1
                prev = n.val
                n = n.next
            elif n.val < prev:
                if f == 2:
                    points.append(p)
                f = 1
                p+=1
                prev = n.val
                n = n.next
            else:
                f = 0
                p+= 1
                prev = n.val
                n = n.next
        if len(points) < 2: return [-1, -1]
        m = 10**6
        for i in range(1, len(points)):
            m = min(m, points[i]-points[i-1])
        return [m, points[-1]-points[0]]