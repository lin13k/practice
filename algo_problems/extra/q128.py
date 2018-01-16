class Solution:
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        from collections import defaultdict
        hashDict = defaultdict(int)
        result = 0
        for n in nums:
            if hashDict[n] == 0:
                left = hashDict[n - 1]
                right = hashDict[n + 1]
                hashDict[n] = left + right + 1
                result = max(result, hashDict[n])
                hashDict[n - left] = hashDict[n]
                hashDict[n + right] = hashDict[n]
        return result


if __name__ == '__main__':
    print(Solution().longestConsecutive([1, 2, 6, 8, 4, 5]))
