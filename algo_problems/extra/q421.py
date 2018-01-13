class Solution:
    def findMaximumXOR(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        result = 0
        mask = 0
        for i in range(31, -1, -1):
            mask = (1 << i) | mask
            # print(mask)
            hashDict = {}
            for n in nums:
                hashDict[n & mask] = 1
            # print(hashDict)
            tmp = result | (1 << i)
            # print(tmp)
            for key in hashDict:
                if key ^ tmp in hashDict:
                    # print('check')
                    result = tmp
                    break
        return result


if __name__ == '__main__':
    print(Solution().findMaximumXOR([14, 11, 7, 2]))
    print(Solution().findMaximumXOR([1, 3, 2]))
