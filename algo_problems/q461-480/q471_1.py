class Solution:
    def makesquare(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        nums.sort(reverse=True)
        s = sum(nums)
        equalLen = s // 4
        if equalLen * 4 != s:
            return False

        if len(nums) < 4:
            return False

        if nums[0] > equalLen:
            return False

        used = [False] * len(nums)

        def pickEdge(i, leftValue):
            if i >= len(nums):
                return leftValue % equalLen == 0

            if used[i]:
                return pickEdge(i + 1, leftValue)

            if leftValue < nums[i]:
                return False

            used[i] = True

            available = [j for j in range(i + 1, len(nums))
                         if not used[j] and nums[j] <= leftValue - nums[i]]
            if leftValue == nums[i]:
                return True
            for x in available:
                result = pickEdge(x, leftValue - nums[i])
                print(x, available, result)
                if result:
                    return True
            used[i] = False
            return False

        for i in range(4):
            print(used)
            if not pickEdge(0, equalLen):
                return False
        return True


if __name__ == '__main__':
    print(Solution().makesquare([5, 5, 5, 5, 4, 4, 4, 4, 3, 3, 3, 3]))
