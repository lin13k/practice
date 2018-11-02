from collections import Counter
import heapq


class Solution:
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        d = Counter(nums)
        q = []
        for key, value in d.items():
            if len(q) == k:
                heapq.heappushpop(q, (value, key))
            else:
                heapq.heappush(q, (value, key))
        result = []
        while len(q) != 0:
            result.append(heapq.heappop(q)[1])
        return result


if __name__ == '__main__':
    print(Solution().topKFrequent([1, 1, 1, 2, 2, 3], 2))
