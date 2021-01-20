from collections import deque

class Queue:
    def __init__(self):
        self.queue = deque()

    def enqueue(self,val):
        return self.queue.appendleft(val)

    def dequeue(self):
        return self.queue.pop()

    def size(self):
        return len(self.queue)

    def print(self):
        return print(self.queue)

    def peek(self):
        return self.queue[-1]

    def rear(self):
        return self.queue[0]

    def isempty(self):
        return print(len(self.queue) == 0)

if __name__ == "__main__":
    q = Queue()
    q.enqueue(10)
    q.enqueue(20)
    q.enqueue(30)
    q.print()
    print(q.size())
    q.dequeue()
    q.print()
    print(q.peek())
    print(q.rear())
    q.isempty()