class Solution:
    def minimumPerimeter(self, neededApples: int) -> int:
        num = neededApples//12
        if num * 12 != neededApples:
            num += 1
        p, apples = 0, 0
        while apples < num:
            p += 1
            apples += p*p
        return p * 8
            