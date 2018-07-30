def fairPay(nums):
    n = len(nums)
    equalNum = sum(nums) // n
    tmpNums = [i - equalNum for i in nums]
    surpluses = {}
    deficits = {}
    for i, val in enumerate(tmpNums):
        if val > 0:
            if val in surpluses:
                surpluses[val].append(i)
            else:
                surpluses[val] = [i]
        if val < 0:
            if val in deficits:
                deficits[val].append(i)
            else:
                deficits[val] = [i]

    def helper(surpluses, deficits, transactions):
        if len(surpluses) == 0:
            return
        for sur, indexes in surpluses.items():
            # check if just match pair exist
            if -sur in deficits:
                popNum = min(len(surpluses[sur]), len(deficits[-sur]))
                sources = None
                targets = None
                sources = surpluses[sur][:popNum]
                surpluses[sur] = surpluses[sur][popNum:]
                targets = deficits[-sur][:popNum]
                deficits[-sur] = deficits[-sur][popNum:]
                transactions.extend(
                    list([sources[i], targets[i], sur]
                         for i in range(len(sources))))
        surpluses = {i: surpluses[i]
                     for i in surpluses if len(surpluses[i]) > 0}
        deficits = {i: deficits[i] for i in deficits if len(deficits[i]) > 0}

        if len(surpluses) == 0:
            return

        sur = max(surpluses.keys())
        deficit = min(deficits.keys())

        target = deficits[deficit].pop()
        if len(deficits[deficit]) == 0:
            deficits.pop(deficit)

        source = surpluses[sur].pop()
        if len(surpluses[sur]) == 0:
            surpluses.pop(sur)

        if sur > -deficit:
            if sur + deficit in surpluses:
                surpluses[sur + deficit].append(source)
            else:
                surpluses[sur + deficit] = [source]
        else:
            if sur + deficit in deficits:
                deficits[sur + deficit].append(target)
            else:
                deficits[sur + deficit] = [target]
        transactions.append([source, target, min(sur, -deficit)])
        return helper(surpluses, deficits, transactions)

    transactions = []
    helper(surpluses, deficits, transactions)
    return transactions


if __name__ == '__main__':
    print(fairPay([15, 60, 30]))
