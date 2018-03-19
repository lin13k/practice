def search(nums, target):
    start = 0
    end = len(nums) - 1
    while start + 1 < end:
        mid = start + (end - start) // 2
        if nums[mid] < target:
            start = mid
        elif nums[mid] >= target:
            end = mid
    if nums[start] == target:
        return start
    if nums[end] == target:
        return end
    return -1


if __name__ == '__main__':
    print(search([1,1,2,2], 0))
    print(search([1,1,2,2], 3))
    print(search([1,2,3,4,5], 1))
    print(search([1,2,3,4,5], 2))
    print(search([1,2,3,4,5], 3))
    print(search([1,2,3,4,5], 4))
    print(search([1,2,3,4,5], 5))
    print(search([1,2,3,4,5,6,7,8], 6))
    print(search([1,2,3,4,5,6,7,8], 7))
    print(search([1,2,3,4,5,6,7,8], 8))