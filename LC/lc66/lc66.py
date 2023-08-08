class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        if digits [-1] != 9:
            digits[-1] += 1
            return digits
        else:
            if len(digits) == 1:
                return [1,0]
            else:
                out = self.plusOne(digits[:-1])
                out.append(0)
                return out