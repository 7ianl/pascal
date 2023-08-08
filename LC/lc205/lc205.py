class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        dict1 = {}
        dict2 = {}
        for i in range(len(s)):
            if s[i] in dict1:
                dict1[s[i]].append(i)
            else:
                dict1[s[i]] = [i]
        for j in range(len(t)):
            if t[j] in dict2:
                dict2[t[j]].append(j)
            else:
                dict2[t[j]] = [j]
        l1 = list(dict1.values())
        l2 = list(dict2.values())
        l1.sort(), l2.sort()
        return (len(l1) == len(l2) and 
                all([ len(l1[i]) == len(l2[i]) and 
                     all([l1[i][j]==l2[i][j] for j in range(len(l1[i]))]) for i in range(len(l1))]) )
        