from heapq import heappush, heappop


class Solution(object):
    def kSmallestPairs(self, nums1, nums2, k):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :type k: int
        :rtype: List[List[int]]
        """
        heap = []
        for n1 in nums1:
            for n2 in nums2:
                if len(heap) < k:
                    heappush(heap, (-n1 - n2, (n1, n2)))
                else:
                    item = max(heappop(heap), (-n1 - n2, (n1, n2)))
                    heappush(heap, item)
        return list(list(i[1]) for i in heap)


if __name__ == '__main__':
    print(Solution().kSmallestPairs([1, 2, 4], [2, 3], 3))
    print(Solution().kSmallestPairs([1, 7, 11], [2, 4, 6], 3))

