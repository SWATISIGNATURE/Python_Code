from collections import deque

class Stack:
    def __init__(self):
        self.stack = deque()

    def push(self,val):
        return self.stack.append(val)

    def pop(self):
        return self.stack.pop()

    def peek(self):
        return self.stack[-1]

    def top(self):
        return self.stack[0]

    def is_empty(self):
        return len(self.stack) == 0

    def size(self):
        return len(self.stack)

    def print(self):
        return self.stack

if __name__ == "__main__":
    s = Stack()
    s.push(6)
    s.push(8)
    s.push(10)
    s.push(14)
    print(s.size())
    print(s.print())
    s.pop()
    print(s.peek())
    print(s.size())
    print(s.print())
    print(s.top())
    print(s.is_empty())
    print((s.size()))
