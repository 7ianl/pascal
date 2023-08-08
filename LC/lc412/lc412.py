class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        res = list()
        f = 'Fizz'
        b = 'Buzz'
        fb = 'FizzBuzz'
        for num in range(1,n+1):
            if not num%3:
                if num % 5:
                    res.append(f)
                else:
                    res.append(fb)
            elif not num%5:
                res.append(b)
            else:
                res.append(str(num))
        return res
        