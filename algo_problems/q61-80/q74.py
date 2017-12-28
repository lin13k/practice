class Solution:
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        return self.binary_search(
            self.binary_pick_list(matrix, target), target)

    def binary_pick_list(self, matrix, target):
        if len(matrix) == 0:
            return []
        m = len(matrix) // 2

        if len(matrix[0]) == 0:
            return []
        if matrix[m][0] <= target and matrix[m][-1] >= target:
            return matrix[m]
        if matrix[m][0] > target:
            return self.binary_pick_list(matrix[:m], target)
        else:
            return self.binary_pick_list(matrix[m + 1:], target)

    def binary_search(self, nums, target):
        if len(nums) == 0:
            return False
        m = len(nums) // 2

        if nums[m] == target:
            return True
        if nums[m] > target:
            return self.binary_search(nums[:m], target)
        else:
            return self.binary_search(nums[m + 1:], target)


if __name__ == '__main__':
    # print(Solution().binary_search([1, 2, 3, 4, 5, 6, 7], 3))
    # print(Solution().binary_search([1, 2, 3, 4, 5, 6, 7], 7))
    # print(Solution().binary_search([1, 2, 3, 4, 5, 6, 7], 8))
    # print(Solution().binary_search([1, 2, 3, 4, 5, 6, 7], 1))
    # print(Solution().binary_search([1, 2, 3, 4, 5, 6, 7], 0))

    print(Solution().searchMatrix([[]],1))
    print(Solution().searchMatrix([[1]],1))
    print(Solution().searchMatrix([[1, 2, 3],
                                    [4, 5,6,7]],4))
