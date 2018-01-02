class Solution:
    def largestRectangleArea(self, heights):
        """
        :type heights: List[int]
        :rtype: int
        """
        heights.append(0)
        stack = [-1]
        result = 0
        for i in range(len(heights)):
            # print('stack', stack)
            while heights[stack[-1]] > heights[i]:
                # print('pop')
                s = stack.pop()
                # print('i', i, 's', s)
                w = i - stack[-1] - 1
                h = heights[s]
                # print('w', w, 'h', h, 'h*w', h * w)
                result = max(result, h * w)
            stack.append(i)
        return result


if __name__ == '__main__':
    print(Solution().largestRectangleArea([1, 2, 3, 2]))
    print(Solution().largestRectangleArea([1, 2, 13, 2]))
    print(Solution().largestRectangleArea([2, 1, 2]))
