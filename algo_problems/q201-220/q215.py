import heapq


class Solution(object):
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        largeHeap = []
        for n in nums:
            heapq.heappush(largeHeap, n)
            if len(largeHeap) > k:
                heapq.heappop(largeHeap)
        return largeHeap[0]
