class Solution:
    def grayCode(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        result = []
        self.recursive_func(n, 0, result)
        return result

    def recursive_func(self, n, num, result):
        if n == 0:
            result.append(num)
            return

        if self.hdistance(num) & 1 == 1:
            self.recursive_func(n - 1, (num << 1) + 1, result)
            self.recursive_func(n - 1, num << 1, result)

        else:
            self.recursive_func(n - 1, num << 1, result)
            self.recursive_func(n - 1, (num << 1) + 1, result)

    def hdistance(self, n):
        result = 0
        while n > 0:
            if n & 1 == 1:
                result += 1
            n >>= 1
        return result

# 3
# 000 0 
# 001 1
# 011 3
# 010 2
# 110 6
# 111 7
# 101 5
# 100 4
# 



if __name__ == '__main__':
    print(Solution().grayCode(2))
    print(Solution().grayCode(3))
    # print(Solution().hdistance(1))
    # print(Solution().hdistance(2))
    # print(Solution().hdistance(3))
    # print(Solution().hdistance(4))
    # print(Solution().hdistance(5))
    # print(Solution().hdistance(6))
    # print(Solution().hdistance(7))
