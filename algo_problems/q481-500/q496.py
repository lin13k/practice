class Solution:
    def nextGreaterElement(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        stack = []
        d = {}
        for k, v in enumerate(nums2):
            while len(stack) > 0 and stack[-1] < v:
                t = stack.pop(-1)
                d[t] = v
            stack.append(v)
        return list(d[i] if i in d else -1 for i in nums1)


if __name__ == '__main__':
    print(Solution().nextGreaterElement([4, 1, 2], [1, 3, 4, 2]))
    print(Solution().nextGreaterElement([2, 4], [1, 2, 3, 4]))
