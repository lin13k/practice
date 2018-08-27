# -*- coding: utf8 -*-
from itertools import combinations


class CardChecker(object):
    """docstring for CardChecker"""
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
        self.sameNumberDict = self.getSameNumberDict()

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

    def getSameNumberDict(self):
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


class BombWithTwoPairPattern(AbstractPattern):
    def check(self):
        result = []
        dic = self.numberDict
        if len(self._cards) < 6:
            return result
        for i in range(13):
            if len(dic[i]) == 4:
                pairList = []
                cpyDic = dic.copy()
                cpyDic.pop(i)
                for k in cpyDic.values():
                    if len(k) >= 2:
                        pairList.append(k[:2])
                pairCom = combinations(pairList, 2)
                for com in pairCom:
                    result.append(dic[i] + sum(com, []))
        return result

    def desc(self):
        return "Bomb with two pair"


class BombWithTwoSinglePattern(AbstractPattern):
    def check(self):
        result = []
        dic = self.numberDict
        if len(self._cards) < 6:
            return result
        for i in range(13):
            if len(dic[i]) == 4:
                cardList = []
                cpyDic = dic.copy()
                cpyDic.pop(i)
                for k in cpyDic.values():
                    if len(k) >= 1:
                        cardList.append(k[:1])
                if 52 in self._cards:
                    cardList.append([52])
                if 53 in self._cards:
                    cardList.append([53])
                coms = combinations(cardList, 2)
                for com in coms:
                    result.append(dic[i] + sum(com, []))
        return result

    def desc(self):
        return "Bomb with two single"


class SinglePattern(AbstractPattern):
    def check(self):
        return [[i] for i in self._cards]

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


class TripleWithSinglePattern(AbstractPattern):
    def check(self):
        result = []
        dic = self.numberDict
        if len(self._cards) <= 3:
            return result
        for i in range(13):
            if len(dic[i]) >= 3:
                cardList = []
                cpyDic = dic.copy()
                cpyDic.pop(i)
                for k in cpyDic.values():
                    if len(k) >= 1:
                        cardList.append(k[:1])
                for card in cardList:
                    result.append(dic[i][:3] + card)

                if 52 in self._cards:
                    result.append(dic[i][:3] + [52])
                if 53 in self._cards:
                    result.append(dic[i][:3] + [53])
        return result

    def desc(self):
        return "Triple with single"


class TripleWithPairPattern(AbstractPattern):
    def check(self):
        result = []
        dic = self.numberDict
        if len(self._cards) <= 3:
            return result
        for i in range(13):
            if len(dic[i]) >= 3:
                pairList = []
                cpyDic = dic.copy()
                cpyDic.pop(i)
                for k in cpyDic.values():
                    if len(k) >= 2:
                        pairList.append(k[:2])
                for pair in pairList:
                    result.append(dic[i][:3] + pair)

        return result

    def desc(self):
        return "Triple with pair"


class SingleStraightPattern(AbstractPattern):
    def check(self):
        result = []
        dic = self.numberDict
        for startNum in range(2, 10):
            if all(len(dic[(startNum + i) % 13]) != 0 for i in range(5)):
                tmp = list(dic[(startNum + i) % 13][0] for i in range(5))
                i = 5
                result.append(tmp[:])
                while len(dic[(startNum + i) % 13]) != 0 and\
                        (startNum + i) % 13 != 1:
                    tmp.append(dic[(startNum + i) % 13][0])
                    i += 1
                    result.append(tmp[:])

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
                result.append(sum(tmp, []))
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
                result.append(sum(tmp, []))
                while len(dic[(startNum + i) % 13]) > 2 and\
                        (startNum + i) % 13 != 1:
                    tmp.append(dic[(startNum + i) % 13][:3])
                    i += 1
                    result.append(sum(tmp, []))

        return result

    def desc(self):
        return "Triple straight"


def PATTERN_LIST(cards):
    # yield SingleStraightPattern(cards)
    for cls in AbstractPattern.__subclasses__():
        yield cls(cards)


def show_cards(cardsDict):
    suits = '♣♦♥♠'
    for key, value in cardsDict.items():
        if value is None:
            continue
        print('%s' % key)
        for cards in value:
            for card in cards:
                if card < 52:
                    suit, num = divmod(card, 13)
                    print('%s %s' % (suits[suit], num), end=',')
                else:
                    print(' BJ' if card == 52 else ' CJ', end=',')
            print()


if __name__ == '__main__':
    cc = CardChecker()
    # print(cc.check([1, 2, 3, 52, 53, 14, 15, 27, 40]))
    # print(cc.check([1, 14, 27, 2, 15, 28, 3, 16]))
    # print(cc.check([1, 2, 3, 4, 5, 6, 7, 14, 15, 16, 17, 18, 28, 29]))
    show_cards(cc.check([1, 2, 3, 4, 5, 6, 7, 8, 9, 14, 15, 16, 17, 18, 28, 29, 27, 40, 52]))
