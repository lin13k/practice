class Solution(object):
    def fourSum(self, nums, target):
        nums.sort()
        result = []
        if len(nums) < 4:
            return result

        for i in range(len(nums) - 3):
            for j in range(i + 1, len(nums) - 2):
                m = j + 1
                n = len(nums) - 1
                while m < n:
                    if nums[i] + nums[j] + nums[m] + nums[n] == target:
                        result.append((nums[i], nums[j], nums[m], nums[n]))
                        n -= 1
                        m += 1
                    elif nums[i] + nums[j] + nums[m] + nums[n] > target:
                        n -= 1
                    else:
                        m += 1

        result = list(set(result))
        return result


if __name__ == '__main__':
    # print(Solution().fourSum([0], 0))
    # print(Solution().fourSum([], 0))
    # print(Solution().fourSum([0,0,0,0], 1))
    # print(Solution().fourSum([0,0,0,0], 0))
    print(Solution().fourSum([-1, 0, 1, 2, -1, -4], -1))
