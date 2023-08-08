"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def connect(self, root: 'Node') -> 'Node':
        def bfs(cur):
            nxt = []
            for x in cur:
                if x.left:
                    nxt.append(x.left)
                if x.right:
                    nxt.append(x.right)
            if len(nxt) == 0: return
            for i in range(len(nxt)-1):
                nxt[i].next = nxt[i+1]
            return bfs(nxt)
        if not root: return root
        bfs([root])
        return root