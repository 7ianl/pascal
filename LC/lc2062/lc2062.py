class Solution:
    def countVowelSubstrings(self, word: str) -> int:
        arr = []
        for i in word:
            if i =='a':
                arr.append(1)
            elif i =='e':
                arr.append(2)
            elif i == 'i':
                arr.append(3)
            elif i == 'o':
                arr.append(4)
            elif i == 'u':
                arr.append(5)
            else:
                arr.append(0)
        res = 0
        L = len(arr)
        for p in range(L):
            f1, f2, f3, f4, f5 = False, False, False, False, False
            acc  = 0
            for i in range(p, L):
                if arr[i] == 0:
                    break
                elif arr[i] == 1:
                    f1 = True
                elif arr[i] == 2:
                    f2 = True
                elif arr[i] == 3:
                    f3 = True
                elif arr[i] == 4:
                    f4 = True
                elif arr[i] == 5:
                    f5 = True
                if f1 and f2 and f3 and f4 and f5:
                    acc += 1
            res += acc
        return res
            
                    