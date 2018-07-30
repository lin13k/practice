def three_sum(nums, target):
    sset = set()
    nums.sort()
    for i in nums:
        sset.add(target - i)

    