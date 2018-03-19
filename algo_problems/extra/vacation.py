from collections import Counter


class Solution:
    def min_vacations(self, cities):
        total = Counter(cities)
        citiesNumber = len(total)
        result = len(cities)
        countTable = {x: 0 for x in total}
        startDate = 0
        # print('citiesNumber', citiesNumber, 'countTable', countTable)
        for i in range(len(cities)):
            # add
            countTable[cities[i]] += 1
            if countTable[cities[i]] == 1:
                # trigger
                citiesNumber -= 1
            # print('i', i, cities[i], countTable)
            # check if fullfil all
            while citiesNumber == 0:
                if citiesNumber == 0:
                    # all included
                    result = min(result, i + 1 - startDate)
                countTable[cities[startDate]] -= 1
                if countTable[cities[startDate]] == 0:
                    citiesNumber += 1
                startDate = startDate + 1
        # print(result)
        return result

        # try remove


if __name__ == '__main__':
    assert(Solution().min_vacations([1, 2, 3, 4, 5]) == 5)
    assert(Solution().min_vacations([1, 2, 3, 5, 5]) == 4)
    assert(Solution().min_vacations([1, 2, 3, 1, 1]) == 3)
    assert(Solution().min_vacations([1, 2, 1, 2]) == 2)
    assert(Solution().min_vacations([1, 1, 1, 1]) == 1)
    assert(Solution().min_vacations([]) == 0)
