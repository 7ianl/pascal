# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        def searchNode(n, key):
            if not n or n.val == key: return n
            elif n.val > key: return searchNode(n.left, key)
            return searchNode(n.right, key)
        def parentNode(n, key):
            if not n or n.val==key: return n
            if n.val > key:
                if n.left and n.left.val == key: return n
                return parentNode(n.left, key)
            else:
                if n.right and n.right.val == key: return n
                return parentNode(n.right, key)
        def treeMinimum(n):
            while n.left:
                n = n.left
            return n 
        def successorNode(n):
            if n.right:
                return treeMinimum(n.right)
            y = parentNode(root, n.val)
            while y.val != n.val and y.right and y.right.val == n.val:
                n = y
                y = parentNode(root, y.val)
            return y
        root = TreeNode(-10**6, None, root)
        n = searchNode(root, key)
        if not n: return root.right
        p = parentNode(root, key)
        if not n.right:
            if p.val > key:
                p.left = n.left
            elif p.val < key:
                p.right = n.left
            else:
                p = n.left
        elif not n.left:
            if p.val > key:
                p.left = n.right
            elif p.val < key:
                p.right = n.right
            else:
                p = n.right
        else:
            y = successorNode(n)
            if y.val == n.right.val:
                n.val = y.val
                n.right = y.right
            else:
                s = y.val
                z = parentNode(root, s)
                z.left = y.right
                n.val = s
        return root.right