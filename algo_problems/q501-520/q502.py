import heapq


class Solution:
    def findMaximizedCapital(self, k, W, Profits, Capital):
        """
        :type k: int
        :type W: int
        :type Profits: List[int]
        :type Capital: List[int]
        :rtype: int
        """
        heap = []
        options = sorted(zip(Capital, Profits))
        for i in range(k):

            while options and options[0][0] <= W:
                heapq.heappush(heap, -options.pop(0)[1])

            if heap:
                W -= heapq.heappop(heap)
        return W



