class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        mem = dict()
        for t in nums1:
            if t in mem:
                mem[t] += 1
            else:
                mem[t] = 1
        res = list()
        for x in nums2:
            if x in mem and mem[x] > 0:
                mem[x] -= 1
                res.append(x)
        return res