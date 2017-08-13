'''
Created on 2017/04/11
https://leetcode.com/problems/two-sum/#/description
@author: Rage-13K
'''


class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        d = dict()
        for i in range(len(nums)):
            d[nums[i]] = d.get(nums[i], []) + [i]

        print(d)
        for i in range(len(nums)):
            tmp = target - nums[i]
            if tmp == nums[i]:
                if len(d[tmp]) >= 2:
                    return d[tmp][:2]
            else:
                if tmp in d:
                	return [i, d[tmp][0]]

if __name__ == '__main__':
    print(Solution().twoSum([2, 7, 11, 15], 9))
    print(Solution().twoSum([3, 3], 6))
    print(Solution().twoSum([2, 5, 5, 11], 10))
