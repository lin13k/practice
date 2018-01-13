class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        m = len(nums1)
        n = len(nums2)
        if m > n:
            return self.findMedianSortedArrays(nums2, nums1)

        max_i = m
        min_i = 0
        half_len = (m + n + 1) // 2
        is_odd = True if (m + n) & 1 == 1 else False
        while True:
            i = (max_i + min_i) // 2
            j = half_len - i
            # 1[2]3 1[2]34
            if i < m and nums1[i] < nums2[j - 1]:
                min_i += 1
            # [1]23 12[3]4
            elif i > 0 and nums1[i - 1] > nums2[j]:
                max_i -= 1
            else:
                if i == 0:
                    max_left = nums2[j - 1]
                elif j == 0:
                    max_left = nums1[i - 1]
                else:
                    max_left = max(nums2[j - 1], nums1[i - 1])
                if is_odd:
                    return max_left / 1.0

                if i == m:
                    min_right = nums2[j]
                elif j == n:
                    min_right = nums1[i]
                else:
                    min_right = min(nums2[j], nums1[i])
                return (max_left + min_right) / 2.0
