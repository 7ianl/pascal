class MyQueue:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.instack = []
        self.outstack = []

    def push(self, x: int) -> None:
        """
        Push element x to the back of queue.
        """
        self.instack.append(x)

    def pop(self) -> int:
        """
        Removes the element from in front of queue and returns that element.
        """
        if self.outstack:
            return self.outstack.pop()
        elif self.instack:
            while self.instack:
                self.outstack.append(self.instack.pop())
            return self.outstack.pop()
        else:
            raise ValueError()

    def peek(self) -> int:
        """
        Get the front element.
        """
        if self.outstack:
            return self.outstack[-1]
        elif self.instack:
            while self.instack:
                self.outstack.append(self.instack.pop())
            return self.outstack[-1]
        else:
            raise ValueError()

    def empty(self) -> bool:
        """
        Returns whether the queue is empty.
        """
        return not self.instack and not self.outstack


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()