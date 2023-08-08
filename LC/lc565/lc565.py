class Solution:
    def arrayNesting(self, nums: List[int]) -> int:
        seen = set()
        loops = [[]]
        i = 0
        for node in nums:
            if node in seen:
                continue
            else:
                loops[i].append(node)
                k = nums[node]
                seen.add(k)
                while k != node:
                    loops[i].append(k)
                    k = nums[k]
                    seen.add(k)
                loops.append([])
                i+=1
        res = 1
        for ls in loops:
            res = max(len(ls), res)
        return res