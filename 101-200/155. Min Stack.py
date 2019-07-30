'''
Design a stack that supports push, pop, top, and retrieving the minimum element in constant time.

push(x) -- Push element x onto stack.
pop() -- Removes the element on top of the stack.
top() -- Get the top element.
getMin() -- Retrieve the minimum element in the stack.

Example:
MinStack minStack = new MinStack();
minStack.push(-2);
minStack.push(0);
minStack.push(-3);
minStack.getMin();   --> Returns -3.
minStack.pop();
minStack.top();      --> Returns 0.
minStack.getMin();   --> Returns -2.
'''

class MinStack(object):

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.nums=[]
        self.min=[]

    def push(self, x):
        """
        :type x: int
        :rtype: void
        """
        self.nums.append(x)
        if self.min:
            self.min.append(min(x,self.min[-1]))
        else:
            self.min.append(x)
        
    def pop(self):
        """
        :rtype: void
        """
        self.nums.pop()
        self.min.pop()
        

    def top(self):
        """
        :rtype: int
        """
        return self.nums[-1]        

    def getMin(self):
        """
        :rtype: int
        """
        return self.min[-1]

# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()

# Runtime: 44 ms, faster than 100.00% of Python online submissions for Min Stack.
# Memory Usage: 14.6 MB, less than 52.55% of Python online submissions for Min Stack.
