class Robot:

    def __init__(self, width: int, height: int):
        self.m = height-1
        self.n = width-1
        self.pos = 0
        self.initial = True
        

    def move(self, num: int) -> None:
        self.initial = False
        self.pos += num
        self.pos %= (self.m*2+self.n*2)
        

    def getPos(self) -> List[int]:
        if self.pos < self.n:
            return [self.pos, 0]
        elif self.pos < self.n + self.m:
            return [self.n, self.pos-self.n]
        elif self.pos < self.n*2 + self.m:
            return [self.n*2+self.m-self.pos, self.m]
        else:
            return [0, self.m*2 + self.n*2 -self.pos]

    def getDir(self) -> str:
        if self.pos == 0:
            if self.initial:
                return "East"
            else:
                return "South"
        elif self.pos <= self.n:
            return "East"
        elif self.pos <= self.n + self.m:
            return "North"
        elif self.pos <= self.n*2 + self.m:
            return "West"
        else:
            return "South"


# Your Robot object will be instantiated and called as such:
# obj = Robot(width, height)
# obj.move(num)
# param_2 = obj.getPos()
# param_3 = obj.getDir()