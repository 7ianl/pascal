class Solution:
    def kthDistinct(self, arr: List[str], k: int) -> str:
        h = dict()
        lst = [1]*len(arr)
        for i, s in enumerate(arr):
            if s in h:
                lst[h[s]] = 0
                lst[i] = 0
            else:
                h[s] = i
        p = 0
        for i in range(len(lst)):
            if lst[i] == 1:
                p += 1
                if p == k:
                    return arr[i]
        return ''