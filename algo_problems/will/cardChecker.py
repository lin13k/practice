class CardChecker(object):
    """docstring for CardChecker"""

    def __init__(self):
        super(CardChecker, self).__init__()

    def check(self, cards):
        '''
        cards: int list
            0 means clubs 1
            1 means clubs 2
            13 means dimand 1
            51 means spade 13
            52 means BJ
            53 means CJ
        return: list of int list
        '''
        self.patterns = list(PATTERN_LIST(cards))
        result = {}
        for pattern in self.patterns:
            result[pattern.desc()] = pattern.check()

        return result


class AbstractPattern(object):
    def __init__(self, cards):
        self._cards = cards
        self.numberCnt = self.getNumberCnt()
        self.numberDict = self.getNumberDict()
        self.sameNumberCnt = self.getSameNumberCnt()

    def check(self):
        raise NotImplementedError()

    def desc(self):
        raise NotImplementedError()

    def getNumberCnt(self):
        cnts = [0 for i in range(13)]
        for card in self._cards:
            if card > 51:
                continue
            cnts[card % 13] += 1
        return cnts

    def getNumberDict(self):
        dic = {i: [] for i in range(13)}
        for card in self._cards:
            if card > 51:
                continue
            dic[card % 13].append(card)
        return dic

    def getSameNumberCnt(self):
        result = {i: [] for i in range(4)}
        cnts = self.numberCnt
        dic = self.numberDict
        for index, cnt in enumerate(cnts):
            if cnt == 0:
                continue
            result[cnt - 1].append(dic[index])
        return result


class RocketPattern(AbstractPattern):
    def check(self):
        if 52 in self._cards and 53 in self._cards:
            return [52, 53]

    def desc(self):
        return "Rocket"


class BombPattern(AbstractPattern):
    def check(self):
        result = []
        cnts = self.numberCnt
        for index, cnt in enumerate(cnts):
            if cnt == 4:
                result.append([i * 13 + index for i in range(4)])
        return result

    def desc(self):
        return "Bombs"


class BombWithPairPattern(AbstractPattern):
    def check(self):
        result = []
        dic = self.numberDict
        snc = self.sameNumberCnt
        if len(self._cards) < 6:
            return result
        for i in range(13):
            if len(dic[i]) == 4:
                pair = None
                for j in range(1, 3):
                    if len(snc[j]) > 0:
                        if not all(
                                k not in snc[j][0][0:2] for k in dic[i][:3]):
                            continue
                        pair = snc[j][0][0:2]
                        break
                if pair is None:
                    continue
                result.append(dic[i] + pair)

        return result

    def desc(self):
        return "Bomb with pair"


class SinglePattern(AbstractPattern):
    def check(self):
        return self._cards

    def desc(self):
        return "Single card"


class PairPattern(AbstractPattern):
    def check(self):
        result = []
        dic = self.numberDict
        for i in range(13):
            if len(dic[i]) >= 2:
                result.append(dic[i][:2])
        return result

    def desc(self):
        return "Pairs"


class TriplePattern(AbstractPattern):
    def check(self):
        result = []
        dic = self.numberDict
        for i in range(13):
            if len(dic[i]) >= 3:
                result.append(dic[i][:3])
        return result

    def desc(self):
        return "Triples"


class TripleWithOnePattern(AbstractPattern):
    def check(self):
        result = []
        dic = self.numberDict
        snc = self.sameNumberCnt
        if len(self._cards) <= 3:
            return result
        for i in range(13):
            if len(dic[i]) >= 3:
                singleCard = None
                for j in range(2):
                    if len(snc[j]) > 0:
                        singleCard = snc[j][0][0]
                        break
                if singleCard is None:
                    for card in self._cards:
                        if card not in dic[i][:3]:
                            singleCard = card
                result.append(dic[i][:3] + [singleCard])

        return result

    def desc(self):
        return "Triple with one"


class TripleWithTwoPattern(AbstractPattern):
    def check(self):
        result = []
        dic = self.numberDict
        snc = self.sameNumberCnt
        if len(self._cards) <= 3:
            return result
        for i in range(13):
            if len(dic[i]) >= 3:
                pair = None
                for j in range(1, 3):
                    if len(snc[j]) > 0:
                        if not all(
                                k not in snc[j][0][0:2] for k in dic[i][:3]):
                            continue
                        pair = snc[j][0][0:2]
                        break
                if pair is None:
                    continue
                result.append(dic[i][:3] + pair)

        return result

    def desc(self):
        return "Triple with two"


class SingleStraightPattern(AbstractPattern):
    def check(self):
        result = []
        dic = self.numberDict
        for startNum in range(2, 10):
            if all(len(dic[(startNum + i) % 13]) != 0 for i in range(5)):
                tmp = list(dic[(startNum + i) % 13][0] for i in range(5))
                i = 5
                while len(dic[(startNum + i) % 13]) != 0 and\
                        (startNum + i) % 13 != 1:
                    tmp.append(dic[(startNum + i) % 13][0])
                    i += 1
                result.append(tmp)

        return result

    def desc(self):
        return "Single straight"


class DoubleStraightPattern(AbstractPattern):
    def check(self):
        result = []
        dic = self.numberDict
        for startNum in range(2, 10):
            if all(len(dic[(startNum + i) % 13]) > 1 for i in range(3)):
                tmp = list(dic[(startNum + i) % 13][:2] for i in range(3))
                i = 3
                while len(dic[(startNum + i) % 13]) > 1 and\
                        (startNum + i) % 13 != 1:
                    tmp.append(dic[(startNum + i) % 13][:2])
                    i += 1
                result.append(sum(tmp, []))

        return result

    def desc(self):
        return "Double straight"


class TripleStraightPattern(AbstractPattern):
    def check(self):
        result = []
        dic = self.numberDict
        for startNum in range(2, 10):
            if all(len(dic[(startNum + i) % 13]) > 2 for i in range(2)):
                tmp = list(dic[(startNum + i) % 13][:3] for i in range(2))
                i = 2
                while len(dic[(startNum + i) % 13]) > 2 and\
                        (startNum + i) % 13 != 1:
                    tmp.append(dic[(startNum + i) % 13][:3])
                    i += 1
                result.append(sum(tmp, []))

        return result

    def desc(self):
        return "Triple straight"


def PATTERN_LIST(cards):
    for cls in AbstractPattern.__subclasses__():
        yield cls(cards)


if __name__ == '__main__':
    cc = CardChecker()
    # print(cc.check([1, 2, 3, 52, 53, 14, 15, 27, 40]))
    # print(cc.check([1, 14, 27, 2, 15, 28, 3, 16]))
    # print(cc.check([1, 2, 3, 4, 5, 6, 7, 14, 15, 16, 17, 18, 28, 29]))
    print(cc.check([1, 2, 3, 4, 5, 6, 7, 14, 15, 16, 17, 18, 28, 29, 27, 40]))
