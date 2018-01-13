class MyCalendarThree:
    def __init__(self):
        self.data = []

    def book(self, start, end):
        self.data.append((start, 's'))
        self.data.append((end, 'e'))
        self.data.sort()  # sort by time
        count = 0
        maxCount = 0
        for eventTime in self.data:
            if eventTime[1] == 's':
                count += 1
                maxCount = max(maxCount, count)
            if eventTime[1] == 'e':
                count -= 1
        print(self.data)
        return maxCount


if __name__ == '__main__':

    testUnit = MyCalendarThree()
    print(testUnit.book(20, 50))  # return 2
    print(testUnit.book(10, 20))  # return 1
    print(testUnit.book(10, 20))  # return 1
    print(testUnit.book(20, 30))  # return 2
    print(testUnit.book(30, 40))  # return 2
    print(testUnit.book(40, 50))  # return 2
    
    