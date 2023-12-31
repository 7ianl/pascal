class Solution:
    def sortArrayByParity(self, A: List[int]) -> List[int]:
        l = 0
        r = len(A) - 1
        while l < r:
            if A[l] % 2:
                A[l], A[r] = A[r], A[l]
                r -= 1
            else:
                l += 1
        return A