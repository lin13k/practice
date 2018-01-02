class Solution:
    def search(self, nums, target):
        left = 0
        right = len(nums) - 1
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == target:
                return True
            elif nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1

        return False

if __name__ == '__main__':
    print(Solution().search([0, 1, 2, 3], 0))
    print(Solution().search([0, 1, 2, 3], 1))
    print(Solution().search([0, 1, 2, 3], 2))
    print(Solution().search([0, 1, 2, 3], 3))
    print(Solution().search([0, 1, 2, 3], -1))
    print(Solution().search([0, 1, 2, 3], 4))