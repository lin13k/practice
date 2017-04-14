class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        m, n = len(nums1), len(nums2)
        if m > n:
            return self.findMedianSortedArrays(nums2, nums1)
        a, b = nums1, nums2

        min_i = i = 0
        max_i = m
        half_len = (m + n + 1) // 2
        is_odd = True if (m + n) % 2 == 1 else False
        while True:
            i = (min_i + max_i) // 2
            j = half_len - i
            if i < m and a[i] < b[j - 1]:
                min_i = i + 1
            elif i > 0 and a[i - 1] > b[j]:
                max_i = i - 1
            else:
                if i == 0:
                    maxLeft = b[j - 1]
                elif j == 0:
                    maxLeft = a[i - 1]
                else:
                    maxLeft = max(a[i - 1], b[j - 1])
                if is_odd:
                    return maxLeft / 1.0

                if i == m:
                    minRight = b[j]
                elif j == n:
                    minRight = a[i]
                else:
                    minRight = min(a[i], b[j])
                return (maxLeft + minRight) / 2.0


if __name__ == '__main__':
    print(Solution().findMedianSortedArrays([1, 2, 3], []), 2)
    print(Solution().findMedianSortedArrays([1, 3], [2]), 2)
    print(Solution().findMedianSortedArrays([1, 3], [2, 5]), 2.5)
    print(Solution().findMedianSortedArrays([1, 2], [3, 4]), 2.5)
    print(Solution().findMedianSortedArrays([], [3, 4]), 3.5)
    print(Solution().findMedianSortedArrays([], [1,2,3,4,5]), 3)
