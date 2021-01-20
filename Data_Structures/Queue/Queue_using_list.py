class Queue:
    def __init__(self):
        self.lst = []

    def enqueue(self,val):
        return self.lst.insert(0,val)

    def dequeue(self):
        return self.lst.pop()

    def peek(self):
        return self.lst[0]

    def isempty(self):
        return print(len(self.lst) == 0)

    def rear(self):
        return self.lst[-1]

    def print(self):
        return print(self.lst)

    def size(self):
        return len(self.lst)



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
