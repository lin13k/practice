class Solution(object):
    def jump(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        jumpTo = 0
        count = 0
        nxtJump = 0
        for i in range(len(nums) - 1):
            nxtJump = max(i + nums[i], nxtJump)
            if i >= jumpTo:
                count += 1
                jumpTo = nxtJump

        return count






if __name__ == '__main__':
    print(Solution().jump([2, 3, 1, 1, 4]))
    print(Solution().jump([1, 1, 1, 2, 1]))
    print(Solution().jump([1, 1, 1]))
    print(Solution().jump([1, 1, 1, 1, 1]))
    print(Solution().jump([3,2,1]))
    print(Solution().jump([1, 1, 2, 1, 1]))
