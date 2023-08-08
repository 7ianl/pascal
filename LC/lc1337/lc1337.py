class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        lists = list()
        for c, row in enumerate(mat):
            lists.append((c, row.count(1)))
        p = sorted(lists, key = lambda x : x[1])
        return [x[0] for x in p[:k]]