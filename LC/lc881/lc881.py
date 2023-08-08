class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()
        res = 0
        while people:
            k = limit - people[-1]
            res += 1
            people.pop()
            if people and k >= people[0]:
                people.pop(0)
        return res