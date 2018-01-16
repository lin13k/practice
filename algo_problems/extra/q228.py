class Solution(object):
    def summaryRanges(self, nums):
        """
        :type nums: List[int]
        :rtype: List[str]
        """
        result = []
        lastInt = None
        headInt = None
        for n in nums:
            if lastInt is not None and n != lastInt + 1:
                if headInt is not None:
                    result.append('%d->%d' % (headInt, lastInt))
                    headInt = None
                else:
                    result.append('%d'% lastInt)
            else:
                if headInt is None:
                    headInt = lastInt
            lastInt = n
        if headInt is not None:
            result.append('%d->%d' % (headInt, lastInt))
            headInt = None
        elif lastInt is not None:
            result.append('%d'% lastInt)
        return result

if __name__ == '__main__':
    print(Solution().summaryRanges([1,2,3,4,6,7,8,9, 11, 24,25,32]))