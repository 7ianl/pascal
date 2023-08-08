class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        N = len(graph)-1
        self.solutions = []
        cur = [[0, []]]
        while cur:
            nxt = []
            for x, path in cur:
                path.append(x)
                if x == N:
                    self.solutions.append(path)
                    continue
                for y in graph[x]:
                    nxt.append([y, path[:]])
            cur = nxt
        return self.solutions