# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")


class ShipUnit:
    def __init__(self, posString, dicMap, shipSet):
        upLeftS, downRightS = posString.split(" ")
        self.upLeft = (int(upLeftS[:-1]), ord(upLeftS[-1]))
        self.downRight = (int(downRightS[:-1]), ord(downRightS[-1]))
        self.hitPoint = (self.downRight[0] + 1 - self.upLeft[0]) * \
                        (self.downRight[1] + 1 - self.upLeft[1])
        self.dicMap = dicMap
        self.shipSet = shipSet
        self.shipSet.add(self)
        self.register()
        self.damaged = False

    def register(self):
        for x in range(self.upLeft[0], self.downRight[0] + 1):
            for y in range(self.upLeft[1], self.downRight[1] + 1):
                self.dicMap[(x, y)] = self

    def damage(self, hitNum):
        self.hitPoint -= hitNum
        self.damaged = True
        if self.hitPoint <= 0:
            self.destroy()

    def destroy(self):
        for x in range(self.upLeft[0], self.downRight[0] + 1):
            for y in range(self.upLeft[1], self.downRight[1] + 1):
                del self.dicMap[(x, y)]
        self.shipSet.remove(self)


class ShipBattles:
    def __init__(self, N, S):
        self.shipSet = set()
        self.dicMap = {}
        self.initShipNum = 0
        if len(S) != 0:
            shipInitStrings = S.split(",")
            self.initShipNum = len(shipInitStrings)
            for string in shipInitStrings:
                ShipUnit(string, self.dicMap, self.shipSet)

    def fireRounds(self, T):
        # remove duplicated t in T
        if len(T) == 0:
            return
        tSet = set(T.split(" "))
        for ts in tSet:
            tx, ty = (int(ts[:-1]), ord(ts[-1]))
            if (tx, ty) not in self.dicMap:
                continue
            ship = self.dicMap[(tx, ty)]
            ship.damage(1)

    def getStatistics(self):
        # return (destroyedNum, onlyDamagedNum)
        shipNum = len(self.shipSet)
        damagedNum = 0
        for ship in self.shipSet:
            damagedNum += 1 if ship.damaged else 0
        return (self.initShipNum - shipNum, damagedNum)


def solution(N, S, T):
    # write your code in Python 3.6
    shipBattles = ShipBattles(N, S)
    shipBattles.fireRounds(T)
    result = shipBattles.getStatistics()
    return "%d,%d" % result
