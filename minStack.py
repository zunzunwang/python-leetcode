class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.ls = []
        self.lm = []

    def push(self, x: int) -> None:
        self.ls.append(x)
        if len(self.lm) < 1 or self.lm[-1] >= x:
            self.lm.append(x)

    def pop(self) -> None:
        r = self.ls.pop()
        if self.lm[-1] == r:
            self.lm.pop()

    def top(self) -> int:
        return self.ls[-1]

    def getMin(self) -> int:
        return self.lm[-1]

"""
    def push(self, x: int) -> None:
        self.l1.append(x)
        if len(self.lm) < 1 or self.lm[-1] > x:
            self.lm.append(x)
        else :
            self.lm.append(self.lm[-1]) 
        
    def pop(self) -> None:
        self.l1.pop()
        self.lm.pop()

    def top(self) -> int:
        return self.l1[-1]
        
    def getMin(self) -> int:
        return self.lm[-1]
"""
# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()