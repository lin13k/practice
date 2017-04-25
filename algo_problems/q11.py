# Given n non-negative integers a1, a2, ..., an,
# where each represents a point at coordinate (i, ai).
# n vertical lines are drawn such that the two endpoints
# of line i is at (i, ai) and (i, 0). Find two lines,
# which together with x-axis forms a container,
# such that the container contains the most water.

# Note: You may not slant the container and n is at least 2.


class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        tmpMax = 0
        i = 0
        j = len(height) - 1
        while i < j:
            tmpN = min(height[i], height[j]) * (j - i)
            if tmpMax < tmpN:
                tmpMax = tmpN

            if height[i] > height[j]:
                j -= 1
            else:
                i += 1

        return tmpMax


if __name__ == '__main__':
    assert(Solution().maxArea([1, 1]) == 1)