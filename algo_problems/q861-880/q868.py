class Solution(object):
    def transpose(self, A):
        """
        :type A: List[List[int]]
        :rtype: List[List[int]]
        """
        return list(map(list, zip(*A)))


if __name__ == '__main__':
    print(Solution().transpose([[1, 2, 3], [4, 5, 6], [7, 8, 9]]))
