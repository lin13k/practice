class Solutions:
    def allocate(self, seats, scores, preferences):
        sortedPreferences = sorted(
            list((scores[i], preferences[i]) for i in range(len(scores))),
            reverse=True)
        noSchool = 0
        for score, pref in sortedPreferences:
            schoolFlag = False
            for school in pref:
                if seats[school] <= 0:
                    continue
                else:
                    schoolFlag = True
                    seats[school] -= 1
                    break
            if not schoolFlag:
                noSchool += 1

        noStudent = sum(seats)

        print(noSchool, noStudent)


if __name__ == '__main__':
    Solutions().allocate(
        [1, 3, 1, 2],
        [99, 78, 83, 86, 92],
        [
            [3, 2, 1],
            [3, 0, 0],
            [2, 0, 1],
            [0, 1, 3],
            [0, 2, 3]
        ]
    )
