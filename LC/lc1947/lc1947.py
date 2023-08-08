class Solution:
    def maxCompatibilitySum(self, students: List[List[int]], mentors: List[List[int]]) -> int:
        def compScore(i, j):
            a = 0
            for x in range(len(students[i])):
                if students[i][x] == mentors[j][x]:
                    a += 1
            return a
        mem = [[0]*len(students) for x in range(len(students))]
        for i in range(len(students)):
            for j in range(len(mentors)):
                mem[i][j] = compScore(i, j)
        @lru_cache(None)
        def dp(m1, m2, r):
            if r == 0: return 0
            res = 0
            for i in range(len(students)):
                if not m1&1<<i:
                    greedy = [-1, -1]
                    for j in range(len(mentors)):
                        if not m2&1<<j:
                            if mem[i][j] > greedy[1]:
                                greedy = [j, mem[i][j]]
                    res = max(res, greedy[1]+dp(m1^1<<i, m2^1<<greedy[0], r-1))
            return res
        return dp(0, 0, len(students))
                    