import sys
class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        if n == 0:
            return 0

        subList = []
        start = 0
        for i in range(n):
            if nums[i] == 0:
                subList.append(nums[start:i])
                start = i + 1
        subList.append(nums[start:])

        tmpMax = -sys.maxsize
        for sub in subList:
            tmpMax = max(tmpMax, self.help(sub))
        if len(subList) > 1 and tmpMax < 0:
            return 0
        return tmpMax

    def help(self, nums):
        n = len(nums)
        table = [[0 for j in range(n)] for i in range(n)]
        tmpMax = -sys.maxsize
        for i in range(n):
            for j in range(i, n):
                if i == j:
                    table[i][i] = nums[i]
                else:
                    table[i][j] = table[i][j - 1] * nums[j]
                tmpMax = max(tmpMax, table[i][j])
        return tmpMax

if __name__ == '__main__':
    print(Solution().maxProduct([1, 2, 3]))
    print(Solution().maxProduct([1, 2, -3]))
    print(Solution().maxProduct([1, 0, -3, -1]))
    print(Solution().maxProduct([-2]))
