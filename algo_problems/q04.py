class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):

        n = len(nums1)
        m = len(nums2)
        for i in range((n + m) // 2):
            if len(nums1) > 0 and len(nums2) > 0:
                tmpInt = nums1.pop(0) if nums1[0] < nums2[0] else nums2.pop(0)
            elif len(nums1) > 0:
                tmpInt = nums1.pop(0)
            else:
                tmpInt = nums2.pop(0)

        if (n + m) % 2 == 1:
            if len(nums1) > 0 and len(nums2) > 0:
                tmpInt = nums1.pop(0) if nums1[0] < nums2[0] else nums2.pop(0)
            elif len(nums1) > 0:
                tmpInt = nums1.pop(0)
            else:
                tmpInt = nums2.pop(0)
            return tmpInt / 1.0
        else:

            if len(nums1) > 0 and len(nums2) > 0:
                tmpInt2 = nums1.pop(0) if nums1[0] < nums2[0] else nums2.pop(0)
            elif len(nums1) > 0:
                tmpInt2 = nums1.pop(0)
            else:
                tmpInt2 = nums2.pop(0)
            return (tmpInt + tmpInt2) / 2.0


if __name__ == '__main__':
    print(Solution().findMedianSortedArrays([1, 3], [2]), 2)
    print(Solution().findMedianSortedArrays([1, 3], [2, 5]), 2.5)
    print(Solution().findMedianSortedArrays([1, 2], [3, 4]), 2.5)
    print(Solution().findMedianSortedArrays([], [3, 4]), 3.5)
