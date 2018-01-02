class Solution:
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: void Do not return anything, modify nums1 in-place instead.
        """
        # print(sorted(nums1 + nums2))

        i = 0
        j = 0
        while len(nums1) > m:
            nums1.pop()
        while len(nums2) > n:
            nums2.pop()

        while i < m and j < n:
            if nums1[i] < nums2[j]:
                i += 1
            elif nums1[i] > nums2[j]:
                nums1.insert(i, nums2[j])
                j += 1
                m += 1
                i += 1
            else:
                i += 1
        if i == m:
            nums1 += nums2[j:]

        # print(nums1)


if __name__ == '__main__':
    Solution().merge([1, 2, 3], 3, [2, 3, 4], 3)
