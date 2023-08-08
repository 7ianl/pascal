class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        l = len(arr)
        if l < 3 or arr[1] <= arr [0]:
            return False
        up = 1
        for i in range(2, l):
            if arr[i] > arr[i-1]:
                if not up:
                    return False
            elif arr[i] < arr[i-1]:
                if up:
                    up = 0
            else:
                return False
        return up == 0
        