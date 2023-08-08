class Solution:
    def isMonotonic(self, A: List[int]) -> bool:
        case = 0
        for i in range(1, len(A)):
            if A[i] == A[i-1]:
                continue
            if A[i] > A[i-1]:
                if case != 1:
                    if case == 0:
                        case = 1
                    else:
                        return False
            if A[i] < A[i-1]:
                if case != 2:
                    if case == 0:
                        case = 2
                    else:
                        return False
        return True
        