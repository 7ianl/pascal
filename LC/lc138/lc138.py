"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Node') -> 'Node':
        def cacheList(head):
            res = list()
            while head:
                res.append(head.val)
                head = head.next
            return res
        def indexList(head):
            index = 0
            out = Node(0, head)
            while head:
                head.val = index
                head = head.next
                index += 1
            return out.next
        def getIndex(head):
            res = list()
            while head:
                if head.random == None:
                    res.append(-1)
                else:
                    res.append(head.random.val)
                head = head.next
            return res
        def getNode(head, index):
            if index:
                head = head.next; index -= 1
                return getNode(head, index)
            return head
        def nodeList(head, indexList):
            res = list()
            for i in indexList:
                if i == -1:
                    res.append(None)
                else:
                    res.append(getNode(head, i))
            return res
        def makeList(head):
            res = Node(0)
            out = Node(0, res)
            while head.next:
                res.val = head.val
                res.next = Node(0)
                head = head.next; res = res.next
            res.val = head.val
            return out.next
        def addRandom(head, nodeList):
            out = Node(0, head)
            index = 0
            L = len(nodeList)
            while index < L:
                head.random = nodeList[index]
                index += 1; head = head.next
            return out.next
        def restoreVals(head, vallist):
            out = Node(0, head)
            L = len(vallist)
            index = 0
            while head:
                head.val = vallist[index]
                head = head.next
                index += 1
            return out.next
        if not head:
            return None
        vallist = cacheList(head)
        head = indexList(head)
        indexlist = getIndex(head)
        copy = makeList(head)
        nodelist = nodeList(copy, indexlist)
        copy = addRandom(copy, nodelist)
        head = restoreVals(head, vallist)
        copy = restoreVals(copy, vallist)
        return copy
                