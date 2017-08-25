class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        tmp = self.search(candidates, target, 0, (), [])
        return [list(i) for i in list(set(tmp))]

    def search(self, candidates, target, sumNumber, combination, result=[]):
        if sumNumber == target:
            result.append(combination)

        if len(candidates) > 0:
            if candidates[0] + sumNumber <= target:
                self.search(candidates, target, sumNumber +
                            candidates[0], combination + (candidates[0],), result)
                self.search(candidates[1:], target, sumNumber +
                            candidates[0], combination + (candidates[0],), result)
            self.search(candidates[1:], target, sumNumber, combination, result)
        return result


if __name__ == '__main__':
    print(Solution().combinationSum([2, 3, 6, 7], 7))
