class CombinationIterator:

    def __init__(self, characters: str, combinationLength: int):
        self.iterator = itertools.combinations(characters, combinationLength)
        self.remaining = math.factorial(len(characters))//(math.factorial(combinationLength)*math.factorial(len(characters)-combinationLength))

    def next(self) -> str:
        self.remaining -= 1
        return ''.join(self.iterator.__next__())
        

    def hasNext(self) -> bool: return self.remaining>0
        


# Your CombinationIterator object will be instantiated and called as such:
# obj = CombinationIterator(characters, combinationLength)
# param_1 = obj.next()
# param_2 = obj.hasNext()