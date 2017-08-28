class Solution(object):
    def permuteUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        result = []
        self.search(nums, (), result)
        return list(set(result))
    
    def search(self, nums, path, result):
        if len(nums) == 1:
            result.append(path+tuple(nums))
        else:
            used = []
            for i in range(len(nums)):
                if nums[i] not in used:
                    self.search(nums[0:i]+nums[i+1:], path + (nums[i],), result)
                    used.append(nums[i])


if __name__ == '__main__':
    # print(Solution().permute([1,2,3]))
    print(Solution().permuteUnique([1,2,3,4]))
    print(Solution().permuteUnique([1,2,3,4,1,1,1,1]))
    print(Solution().permuteUnique([3,3,0,0,2,3,2]))
