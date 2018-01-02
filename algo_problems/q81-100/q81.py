class Solution:
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: bool
        """
        left = 0
        right = len(nums) - 1
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == target:
                return True
            
            if nums[mid] < nums[right]:
                # normal between mid~right
                if nums[mid] <= target <= nums[right]:
                    left = mid + 1
                else:
                    right = mid - 1

            elif nums[mid] > nums[right]:
                # normal between left~mid
                if nums[left] <= target <= nums[mid]:
                    right = mid - 1
                else:
                    left = mid + 1
            else:
                right -= 1


        return False


if __name__ == '__main__':
    print(Solution().search([4, 5, 6, 7, 0, 1, 2, 3], 0))
    print(Solution().search([4, 5, 6, 7, 0, 1, 2, 3], 1))
    print(Solution().search([4, 5, 6, 7, 0, 1, 2, 3], 2))
    print(Solution().search([0, 1, 2, 3], 3))
    print(Solution().search([3, 0, 1, 2], 3))
    print(Solution().search([4, 5, 6, 7, 0, 1, 2, 3], 3))
    print(Solution().search([4, 5, 6, 7, 0, 1, 2, 3], 4))
    print(Solution().search([4, 5, 6, 7, 0, 1, 2, 3], 5))
    print(Solution().search([4, 5, 6, 7, 0, 1, 2, 3], 6))
    print(Solution().search([4, 5, 6, 7, 0, 1, 2, 3], 7))

    print(Solution().search([4, 5, 6, 7, 0, 1, 2, 3, 4], 0))
    print(Solution().search([4, 5, 6, 7, 0, 1, 2, 3, 4], 1))
    print(Solution().search([4, 5, 6, 7, 0, 1, 2, 3, 4], 2))
    print(Solution().search([4, 5, 6, 7, 0, 1, 2, 3, 4], 3))
    print(Solution().search([4, 5, 6, 7, 0, 1, 2, 3, 4], 4))
    print(Solution().search([4, 5, 6, 7, 0, 1, 2, 3, 4], 5))
    print(Solution().search([4, 5, 6, 7, 0, 1, 2, 3, 4], 6))
    print(Solution().search([4, 5, 6, 7, 0, 1, 2, 3, 4], 7))

    print(Solution().search([0,0,0,0,0,0,0,0,0,0,0,0,0,0], 1))
    print(Solution().search([], 1))
    print(Solution().search([1, 1, 3, 1], 3))
    print(Solution().search([1, 1, 1, 3, 1], 3))
    print(Solution().search([1, 3, 1, 1, 1], 3))
