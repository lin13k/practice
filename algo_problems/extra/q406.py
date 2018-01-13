class Solution:
    def reconstructQueue(self, people):
        """
        :type people: List[List[int]]
        :rtype: List[List[int]]
        """
        # [[7,0], [4,4], [7,1], [5,0], [6,1], [5,2]]
        # (h, n)
        # sort by h decreasing, then sort by n increasing
        people.sort(key=lambda x: (-x[0], x[1]))
        result = []
        while len(people) != 0:
            tmp = people.pop(0)
            result.insert(tmp[1], tmp)
        return result


if __name__ == '__main__':
    print(Solution().reconstructQueue(
        [[7, 0], [4, 4], [7, 1], [5, 0], [6, 1], [5, 2]]))
