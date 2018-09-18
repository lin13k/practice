import collections


class Solution:
    def lenLongestFibSubseq(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        table = collections.defaultdict(lambda: 2)
        indexDict = {v: k for k, v in enumerate(A)}
        result = 0
        for i, v in enumerate(A):
            for j in range(i):
                t = v - A[j]
                k = indexDict.get(t, None)
                if k is not None and j < k:
                    cand = table[k, i] = table[j, k] + 1
                    result = max(result, cand)
        return result


if __name__ == '__main__':
    print(Solution().lenLongestFibSubseq([1, 2, 3, 4, 5, 6, 7, 8]))
