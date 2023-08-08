class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        l = len(arr)-1
        p1 = l
        d = 0
        res = []
        for i in range(len(arr)):
            if arr[i] > x:
                p1 = i
                break
        p2 = p1 - 1
        for j in range(k):
            if (p2 < 0):
                res.append(arr[p1])
                p1 =p1+ 1
            elif (p1 > l):
                res.append(arr[p2])
                p2 =p2- 1
            elif (arr[p1] - x < x - arr[p2]):
                res.append(arr[p1])
                p1 =p1+ 1
            else:
                res.append(arr[p2])
                p2=p2-1
        res.sort()
        return res