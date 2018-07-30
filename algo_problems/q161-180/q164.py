class Solution(object):
    def maximumGap(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums = list(set(nums))
        n = len(nums)
        if n <= 1:
            return 0
        maxN = max(nums)
        minN = min(nums)
        bucketSize = (maxN - minN) // (n - 1)
        bucketNum = (maxN - minN) // bucketSize + 1

        buckets = [[False, None, None] for i in range(bucketNum)]

        for num in nums:
            index = (num - minN) // bucketSize
            if buckets[index][0] is False:
                buckets[index][0] = True
                buckets[index][1] = num
                buckets[index][2] = num
            else:
                buckets[index][1] = min(buckets[index][1], num)
                buckets[index][2] = max(buckets[index][2], num)

        gap = 0
        currentBucket = buckets[0]
        for i in range(1, bucketNum):
            if buckets[i][0] is False:
                continue
            gap = max(gap, buckets[i][1] - currentBucket[2])
            currentBucket = buckets[i]
        return gap


if __name__ == '__main__':
    print(Solution().maximumGap([3, 6, 9, 1]))
    print(Solution().maximumGap([1, 1, 1, 1, 1, 5, 5, 5, 5, 5]))
