"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def levelOrder(self, root: 'Node') -> List[List[int]]:
        if not root:
            return []
        stack = [[root]]
        res = []
        while stack:
            layer, nxt = [], []
            l = stack.pop(0)
            for n in l:
                if n.children:
                    nxt.extend(n.children)
                layer.append(n.val)
            res.append(layer)
            if len(nxt):
                stack.append(nxt)
        return res