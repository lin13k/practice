class Solution(object):
    def countRangeSum(self, nums, lower, upper):
        """
        :type nums: List[int]
        :type lower: int
        :type upper: int
        :rtype: int
        """
        sums = [0]
        for n in nums:
            sums.append(sums[-1] + n)
        nums = sums

        def helper(lo, hi):
            mid = (lo + hi) // 2
            if mid == lo:
                return 0
            count = helper(lo, mid) + \
                helper(mid, hi)
            i = mid
            j = mid
            for left in nums[lo:mid]:
                while i < hi and nums[i] - left < lower:
                    i += 1
                while j < hi and nums[j] - left <= upper:
                    j += 1
                count += j - i
            nums[lo:hi] = sorted(nums[lo:hi])
            return count
        return helper(0, len(nums))


if __name__ == '__main__':
    print(Solution().countRangeSum([-2, 5, -1], -2, 2))
