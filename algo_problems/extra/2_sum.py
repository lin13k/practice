class Solution(object):
    def twoSum(self, nums, target):

        dic = {}
        for index, value in enumerate(nums):
            dic[target - value] = index

        print(dic)
        for index, num in enumerate(nums):
            if num in dic and dic[num] != index:
                return [index, dic[num]]
        return []



if __name__ == '__main__':
    print(Solution().twoSum([2,7,11,15], 9))