class Stack:
    def __init__(self):
        self.data = []

    def push(self, value):
        self.data.append(value)

    def pop(self):
        return self.data.pop()

    def clear(self):
        self.data.clear()

    def peek(self):
        return self.data[-1]

    @property
    def length(self):
        return len(self.data)

s = Stack()
s.push("Abc")
s.push("Pqr")
s.push("Xyz")
print(s.pop())
print(s.peek())
print(s.length)




