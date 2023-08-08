class Solution:
    def makeFancyString(self, s: str) -> str:
        lst = list(s)
        current = lst[0]
        if len(lst) < 3:
            return s
        delete = set()
        for i in range(len(lst)-2):
            if lst[i] == lst[i+1] ==lst[i+2]:
                delete.add(i)
        res = []
        for j in range(len(lst)):
            if j not in delete:
                res.append(lst[j])
        return ''.join(res)