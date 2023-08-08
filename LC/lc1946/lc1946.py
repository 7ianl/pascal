class Solution:
    def maximumNumber(self, num: str, change: List[int]) -> str:
        options = {}
        indiff = {}
        for i in range(len(change)):
            if change[i] > i:
                options[str(i)] = str(change[i])
            elif change[i] == i:
                indiff[str(i)] = str(i) 
        started = False
        lst = list(num)
        for j in range(len(num)):
            if lst[j] in options:
                lst[j] = options[lst[j]]
                started = True
            elif started and lst[j] not in indiff:
                break
            else:
                continue
        return ''.join(lst)