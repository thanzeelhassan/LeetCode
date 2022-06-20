class MyQueue:
    def __init__(self):
        self.stack1 = []

    def push(self, x: int) -> None:
        self.stack1.append(x)

    def pop(self) -> int:
        temp = self.stack1[0]
        del self.stack1[0]
        return temp

    def peek(self) -> int:
        return self.stack1[0]

    def empty(self) -> bool:
        if self.stack1:
            return False
        return True

# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()
