

def search(nums, target):
    start = 0
    end = len(nums) - 1
    while end >= start:
        mid = (start + end) // 2
        if nums[mid] == target:
            return True
        if nums[mid] < target:
            start = mid + 1
        if nums[mid] > target:
            end = mid - 1
    return False

if __name__ == '__main__':
    print(search([1,1,2,2], 0))
    print(search([1,2,3,4,5], 1))
    print(search([1,2,3,4,5], 0))
    print(search([1,2,3,4,5], 6))
    print(search([1,2,3,4,5], 2))
    print(search([1,2,3,4,5], 3))
    print(search([1,2,3,4,5], 4))
    print(search([1,2,3,4,5], 5))
    print(search([1,2,3,4,5,6,7,8], 6))
    print(search([1,2,3,4,5,6,7,8], 7))
    print(search([1,2,3,4,5,6,7,8], 8))