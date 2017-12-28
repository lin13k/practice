class Solution:
    def combine(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """
        result = []
        self.recursive_combine(n, k, [], result)
        return result

    def recursive_combine(self, n, k, added_list, result_list):
        if k <= 0:
            result_list.append(added_list)
            return
        if n == k:
            result_list.append(added_list + [i for i in range(n, 0, -1)])
            return

        for i in range(n, k - 1, -1):
            self.recursive_combine(i - 1, k - 1, added_list + [i], result_list)


if __name__ == '__main__':
    print(Solution().combine(4, 2))
