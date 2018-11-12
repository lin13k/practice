class Solution:
    def maxNumber(self, nums1, nums2, k):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :type k: int
        :rtype: List[int]
        """

        tmpLt = []
        for i in range(k + 1):
            j = k - i
            if i <= len(nums1) and j <= len(nums2):
                tmpLt.append(self.merge(self.greedy(
                    nums1, i), self.greedy(nums2, j)))
        return max(tmpLt)

    def greedy(self, nums, n):
        dropCnt = len(nums) - n
        outLt = []
        for num in nums:
            while (dropCnt != 0 and len(outLt) != 0 and
                    outLt[-1] < num):
                outLt.pop(-1)
                dropCnt -= 1
            outLt.append(num)
        return outLt[:n]

    def merge(self, a, b):
        return [max(a, b).pop(0) for _ in a + b]


if __name__ == '__main__':
    # print(Solution().greedy([8, 6, 9], 1))

    print(Solution().maxNumber([8, 6, 9], [1, 7, 5], 3))
