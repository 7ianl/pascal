# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def generateTrees(self, n: int) -> List[Optional[TreeNode]]:
        def indexPairs(k):
            return list(set([(i, k-i-1) for i in range(k)]))
        def shift(t, s):
            if not t: return t
            else: return TreeNode(t.val+s, shift(t.left, s), shift(t.right, s))
        res = {0:[None]}
        for i in range(1, n+1):
            acc = []
            for p, q in indexPairs(i):
                for t1 in res[p]:
                    for t2 in res[q]:
                        acc.append(TreeNode(p+1, t1, shift(t2, p+1)))
            res[i] = acc
        return res[n]