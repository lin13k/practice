import math


class Solution(object):
    def isConvex(self, points):
        """
        :type points: List[List[int]]
        :rtype: bool
        """
        


if __name__ == '__main__':
    print(Solution().isConvex(
        [[0, 0], [0, 1], [1, 1], [1, 0]]))

    # print(Solution().isConvex(
    #     [[0, 0], [0, 10], [10, 10], [10, 0], [5, 5]]))

    print(Solution().isConvex(
        [[0, 0], [1, 0], [1, 1], [-1, 1], [-1, 0]]))
