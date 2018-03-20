class Solution(object):
    def minTotalDistance(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        locations = []
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == 1:
                    locations.append((i, j))
        n = len(locations)
        sum_x, sum_y = 0, 0
        for location in locations:
            sum_x += location[0]
            sum_y += location[1]

        pos_x = [location[0] for location in locations]
        pos_y = [location[1] for location in locations]
        pos_x.sort()
        pos_y.sort()
        best_x = pos_x[n // 2]
        best_y = pos_y[n // 2]

        print(best_x, best_y)

        distance = 0
        for location in locations:
            distance += abs(location[0] - best_x)
            distance += abs(location[1] - best_y)
        return distance


if __name__ == '__main__':
    grid = [
        [1, 0, 0, 0, 1],
        [0, 0, 0, 0, 0],
        [0, 0, 1, 0, 0]
    ]
    print(Solution().minTotalDistance(grid))
