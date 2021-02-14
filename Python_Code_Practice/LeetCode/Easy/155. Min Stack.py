"""
Design a stack that supports push, pop, top, and retrieving the minimum element in constant time.
push(x) -- Push element x onto stack.
pop() -- Removes the element on top of the stack.
top() -- Get the top element.
getMin() -- Retrieve the minimum element in the stack.
Example 1:
Input
["MinStack","push","push","push","getMin","pop","top","getMin"]
[[],[-2],[0],[-3],[],[],[],[]]
Output
[null,null,null,null,-3,null,0,-2]
Explanation
MinStack minStack = new MinStack();
minStack.push(-2);
minStack.push(0);
minStack.push(-3);
minStack.getMin(); // return -3
minStack.pop();
minStack.top();    // return 0
minStack.getMin(); // return -2
Constraints:
Methods pop, top and getMin operations will always be called on non-empty stacks.
"""

from collections import deque


class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.deq = deque()

    def push(self, x: int) -> None:
        self.deq.append(x)

    def pop(self) -> None:
        return self.deq.pop()

    def top(self) -> int:
        if len(self.deq) > 0:
            return self.deq[len(self.deq) - 1]
        else:
            return None

    def getMin(self) -> int:
        if len(self.deq) > 0:
            return min(self.deq)
        else:
            return None

# Your MinStack object will be instantiated and called as such:
minStack = MinStack()
minStack.push(-2)
minStack.push(0)
minStack.push(-3)
print(minStack.getMin()) # return -3
print(minStack.pop())
print(minStack.top())   # return 0
print(minStack.getMin()) # return -2s