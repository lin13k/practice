class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        leftSum = 0
        leftMax = 0
        rightSum = 0
        rightMax = 0
        totalSum = 0
        n = len(height) - 1
        for i in range(len(height)):
            totalSum += height[i]

            leftMax = height[i] if height[i] > leftMax else leftMax
            leftSum += leftMax

            rightMax = height[n - i] if height[n - i] > rightMax else rightMax
            rightSum += rightMax
        return leftSum + rightSum - (rightMax * (n + 1)) - totalSum


if __name__ == '__main__':
    print(Solution().trap([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]))
    print(Solution().trap([2, 0, 2]))
    print(Solution().trap([4, 2, 3]))
