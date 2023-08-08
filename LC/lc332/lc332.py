class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        self.solution = []
        L = len(tickets)+1
        g = collections.defaultdict(list)
        for x, y in tickets:
            g[x].append([y, True])
        g["#"] = [["JFK", True]]
        for x in g.values():
            x.sort(key = lambda x: x[0])
        def dfs(airport, prev, prev_index):
            self.solution.append(airport)
            if len(self.solution) == L: return True
            for i, (nxt, status) in enumerate(g[airport]):
                if status:
                    g[airport][i][1] = False
                    if dfs(nxt, airport, i):
                        return True
            self.solution.pop()
            g[prev][prev_index][1] = True
            return False
        dfs("JFK", "#", 0)
        return self.solution
                    
                
            
            
            
                