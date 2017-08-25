class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        result = []
        self.search(sorted(candidates), target, [], result, 0)
        return result

    # use index to remove duplicated result
    def search(self, candidates, target, path, result, index):
        if target < 0:
            return
        if target == 0:
            result.append(path)
            return

        for i in range(index, len(candidates)):
            if candidates[i] <= target:
                self.search(candidates, target -
                            candidates[i], path + [candidates[i]], result, i)
            else:
                break


if __name__ == '__main__':
    print(Solution().combinationSum([2, 3, 6, 7], 7))
