class Solution(object):
    def search(self, nums, target):
        return -1 if target not in nums else nums.index(target)


if __name__ == '__main__':
    print(Solution().search([1, 3], 0))
    print(Solution().search([0, 1, 2, 3], 0))
    print(Solution().search([1], 1))
