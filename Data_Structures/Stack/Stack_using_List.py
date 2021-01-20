# Here we are implementing stack using python Array/List
class Stack:
    def __init__(self):
        self.lst = []

    def push(self,val):
        self.lst.append(val)
        return self.lst

    def pop(self):
        return self.lst.pop()

    def peek(self):
        return self.lst[-1]

    def top(self):
        return self.lst[0]

    def is_empty(self):
        return self.top() == None

    def size(self):
        return len(self.lst)

    def print(self):
        return self.lst

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




