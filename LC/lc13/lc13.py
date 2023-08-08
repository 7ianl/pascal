class Solution:
    def romanToInt(self, s: str) -> int:
        output = 0
        s += 'N'
        while s[0] == 'M':
            output += 1000; s = s[1:]
        if s[:2] == 'CM':
            output += 900; s = s[2:]
        if s[0] == 'D':
            output += 500; s = s[1:]
        if s[:2] == 'CD':
            output += 400; s = s[2:]
        while s[0] == 'C':
            output += 100; s = s[1:]
        if s[:2] == 'XC':
            output += 90; s = s[2:]
        if s[0] == 'L':
            output += 50; s = s[1:]
        if s[:2] == 'XL':
            output += 40; s = s[2:]
        while s[0] == 'X':
            output += 10; s = s[1:]
        if s[:2] == 'IX':
            output += 9; s = s[2:]
        if s[0] == 'V':
            output += 5; s = s[1:]
        if s[:2] == 'IV':
            output += 4; s = s[2:]
        while s[0] == 'I':
            output += 1; s = s[1:]
        return output