class Solution:
    def duplicateZeros(self, arr: List[int]) -> None:
        """
        Do not return anything, modify arr in-place instead.
        """
        zeroes = 0
        for i in range(len(arr)):
            if arr[i] == 0:
                zeroes += 1
        l = len(arr)
        l1 = l-1
        arr.extend([0]*zeroes)
        l2 = l1 + zeroes
        while l2 >= 0:
            if not arr[l1]:
                arr[l2]=0; arr[(l2-1)] = 0
                l2 -= 2; l1-=1
            else:
                arr[l2] = arr[l1]
                l2 -= 1; l1-=1
        del arr[l:]
                
        