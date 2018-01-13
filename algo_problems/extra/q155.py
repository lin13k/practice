from heapq import heappush, heapify

class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self._stack = []
        self._heap = []

    def push(self, x):
        """
        :type x: int
        :rtype: void
        """
        self._stack.append(x)
        heappush(self._heap, x)

    def pop(self):
        """
        :rtype: void
        """
        tmp = self._stack.pop(-1)
        self._heap.pop(self._heap.index(tmp))
        heapify(self._heap)
        # print('pop', tmp)

    def top(self):
        """
        :rtype: int
        """
        return self._stack[-1]
        

    def getMin(self):
        """
        :rtype: int
        """
        return self._heap[0]
        

minStack = MinStack();
minStack.push(-2)
minStack.push(0)
minStack.push(-3)
minStack.getMin()#   --> Returns -3.
minStack.pop()
minStack.top()#      --> Returns 0.
minStack.getMin()#   --> Returns -2.