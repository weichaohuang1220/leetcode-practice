class MyQueue:
    def __init__(self):
        self.a = []
        self.b = []

    def push(self, x: int) -> None:
        self.a.append(x)
#a b2个栈
#每次在peek和pop之前需要检查b是否为空.yes就把a的元素加入b No则直接弹出b中元素
    def move(self):
        if not self.b:
            while self.a:
                self.b.append(self.a.pop())

    def pop(self) -> int:
        self.move()
        return self.b.pop()

    def peek(self) -> int:
        self.move()
        return self.b[-1]

    def empty(self) -> bool:
        return True if len(self.a) == 0 and len(self.b) == 0 else False

# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()