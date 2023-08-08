class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        l = len(arr) - 1
        trs = arr[l]
        arr[l] = -1
        l -= 1
        while l >= 0:
            arr[l], trs = trs, max(arr[l], trs)
            l -= 1
        return arr