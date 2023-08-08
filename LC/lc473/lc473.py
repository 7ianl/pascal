class Solution:
    def makesquare(self, matchsticks: List[int]) -> bool:
        matchsticks.sort(reverse=True)
        S=sum(matchsticks)
        if S%4: return False
        p = S//4
        @cache
        def dfs(m, r, t):
            if r == 0: return True
            if t == 0: return dfs(m, r, p)
            for i in range(len(matchsticks)):
                if not m&1<<i and matchsticks[i] <= t:
                    if dfs(m^1<<i, r-1, t-matchsticks[i]):
                        return True
            return False
        return dfs(0, len(matchsticks), p)