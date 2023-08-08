class Solution:

    def __init__(self, nums: List[int]):
        self.original = nums
        self.p = list(self.original)
        self.l = len(nums)


    def reset(self) -> List[int]:
        self.p = list(self.original)
        return self.original

    def shuffle(self) -> List[int]:
        for i in range(self.l-1, 0, -1):
            j = random.randint(0, i)
            self.p[j], self.p[i] = self.p[i], self.p[j]
        return self.p


# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.reset()
# param_2 = obj.shuffle()