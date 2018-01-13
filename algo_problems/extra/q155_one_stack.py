
class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self._stack = []
        self._curmin = None

    def push(self, x):
        """
        :type x: int
        :rtype: void
        """
        if self._curmin is None:
            self._curmin = x
        else:
            self._curmin = min(self._curmin, x)
        self._stack.append((x, self._curmin))

    def pop(self):
        """
        :rtype: void
        """
        self._stack.pop()
        self._curmin = self.getMin()

    def top(self):
        """
        :rtype: int
        """
        return self._stack[-1][0]

    def getMin(self):
        """
        :rtype: int
        """
        if len(self._stack) == 0:
            return None
        return self._stack[-1][1]


["MinStack","push","push","push","top","pop","getMin","pop","getMin","pop","push","top","getMin","push","top","getMin","pop","getMin"]
[[],[2147483646],[2147483646],[2147483647],[],[],[],[],[],[],[2147483647],[],[],[-2147483648],[],[],[],[]]