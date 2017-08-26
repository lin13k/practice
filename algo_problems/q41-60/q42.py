class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        hStack = []
        totalValue = 0
        for i in range(1, len(height)):
            if height[i - 1] < height[i]:
                # go up
                level = height[i - 1]
                while len(hStack) > 0 and hStack[-1][0] <= height[i]:
                    preHeight = hStack.pop()
                    totalValue += (preHeight[0] - level) * (i - preHeight[1] - 1)
                    level = preHeight[0]
                if len(hStack) > 0 and hStack[-1][0] > height[i]:
                    totalValue += (height[i] - level) * (i - hStack[-1][1] - 1)
                hStack.append((height[i], i))
            elif height[i - 1] > height[i]:
                # go down
                hStack.append((height[i - 1], i - 1))
        return totalValue


if __name__ == '__main__':
    print(Solution().trap([0,1,0,2,1,0,1,3,2,1,2,1]))
    print(Solution().trap([2,0,2]))
    print(Solution().trap([4,2,3]))