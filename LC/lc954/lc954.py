class Solution:
    def canReorderDoubled(self, arr: List[int]) -> bool:
        def helper(arr):
            L = len(arr)
            def binSearch(key):
                lo, hi = 0, L-1
                while lo <= hi:
                    mid = (lo + hi)//2
                    if arr[mid] < key:
                        lo = mid + 1
                    elif arr[mid] > key:
                        hi = mid - 1
                    else:
                        return mid
                return None
            arr.sort()
            mem = dict()
            for e in arr:
                if e in mem:
                    mem[e] += 1
                else:
                    mem[e] = 1
            for j in range(L):
                if mem[arr[j]] > 0:
                    mem[arr[j]] -= 1
                    k = binSearch(arr[j]*2)
                    if k == None or mem[arr[k]] == 0:
                        return False
                    else:
                        mem[arr[k]] -= 1
                else:
                    continue
            return True
        arr1, arr2 = [], []
        for e in arr:
            if e < 0:
                arr1.append(-e)
            else:
                arr2.append(e)
        return helper(arr1) and helper(arr2)