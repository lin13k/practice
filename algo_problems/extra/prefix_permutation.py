class Solution:
    def check_prefix_permutation(self, numbers):
        for n in range(len(numbers)):
            if numbers[n] == n + 1:
                continue
            # print('main', n, numbers[n] - 1)
            if not self.swap(numbers, n, numbers[n] - 1):
                return False
        return True

    def swap(self, numbers, x, y):
        # print('sub', x, y)
        if x not in range(len(numbers)) or y not in range(len(numbers)):
            return False
        if numbers[x] == numbers[y]:
            return False
        if x == y:
            return False
        else:
            numbers[x], numbers[y] = numbers[y], numbers[x]
            if numbers[y] - 1 != x:
                self.swap(numbers, x, numbers[x] - 1)
        return True


if __name__ == '__main__':
    assert(Solution().check_prefix_permutation([1, 2]) == True)
    assert(Solution().check_prefix_permutation([4, 3, 1, 2]) == True)
    assert(Solution().check_prefix_permutation([3, 1, 2]) == True)
    assert(Solution().check_prefix_permutation([5, 1, 2]) == False)
    assert(Solution().check_prefix_permutation([5, 3, 4, 1, 2]) == True)
    assert(Solution().check_prefix_permutation([2, 2]) == False)
    assert(Solution().check_prefix_permutation([3, 2]) == False)
