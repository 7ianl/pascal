"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        seen = dict()
        def dfs(n, copy):
            seen[n.val]=copy
            for p in n.neighbors:
                if p.val not in seen:
                    new = Node(p.val)
                    copy.neighbors.append(new)
                    dfs(p, new)
                else:
                    copy.neighbors.append(seen[p.val])
        if not node: return None    
        res = Node(node.val)
        dfs(node, res)
        return res