class MinStack:

    def __init__(self):
        self.stack=[]
        self.minstack=[]
        

    def push(self, value: int) -> None:

        self.stack.append(value)
        
        if not self.minstack:
            self.minstack.append(value)

        else:
            min_value=min(self.stack[-1],self.minstack[-1])
        
            self.minstack.append(min_value)

    def pop(self) -> None:
        self.stack.pop()
        self.minstack.pop()

    def top(self) -> int:
        return self.stack[-1]      

    def getMin(self) -> int:
        return self.minstack[-1]
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(value)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()