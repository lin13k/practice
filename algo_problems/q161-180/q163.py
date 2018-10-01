class Solution:
    def findMissingRanges(self, nums, lower, upper):
        """
        :type nums: List[int]
        :type lower: int
        :type upper: int
        :rtype: List[str]
        """
        result = []
        if len(nums) == 0:
            return [str(lower)] if lower == upper else ['%d->%d' % (lower, upper)]
        prev = lower - 1
        for i, num in enumerate(nums):
            if num <= prev:
                continue
            if prev != num - 1:
                if num - prev == 2:
                    result.append(str(prev + 1))
                else:
                    result.append("%d->%d" % (prev + 1, num - 1))
            prev = num
        if upper != nums[-1]:
            if upper - nums[-1] == 1:
                result.append(str(upper))
            else:
                result.append("%d->%d" % (nums[-1] + 1, upper))
        return result
