import random


def sub_partition(array, start, end, idx_pivot):
    'returns the position where the pivot winds up'

    if not (start <= idx_pivot <= end):
        raise ValueError('idx pivot must be between start and end')

    array[start], array[idx_pivot] = array[idx_pivot], array[start]
    pivot = array[start]
    i = start + 1
    j = start + 1

    while j <= end:
        if array[j] <= pivot:
            array[j], array[i] = array[i], array[j]
            i += 1
        j += 1

    array[start], array[i - 1] = array[i - 1], array[start]
    return i - 1


def quicksort(array, start=0, end=None):

    if end is None:
        end = len(array) - 1

    if end - start < 1:
        return

    idx_pivot = random.randint(start, end)
    i = sub_partition(array, start, end, idx_pivot)
    # print array, i, idx_pivot
    quicksort(array, start, i - 1)
    quicksort(array, i + 1, end)


class Solution(object):
    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        flag = False
        for i in range(len(nums) - 2, -1, -1):
            if nums[i] < nums[i + 1]:
                flag = True
                targetNum = nums[i]
                quicksort(nums, i)
                for j in range(i, len(nums)):
                    if nums[j] > targetNum:
                        nums.insert(i, nums.pop(j))
                        break
                break
        if not flag:
            nums.reverse()


if __name__ == '__main__':
    a = [1, 2, 3]
    Solution().nextPermutation(a)
    print(a)

    a = [1, 3, 2]
    Solution().nextPermutation(a)
    print(a)