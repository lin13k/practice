from collections import Counter, defaultdict


def electionWinner(votes):
    c = Counter(votes)
    cnts = defaultdict(list)
    for k, v in c.items():
        cnts[v].append(k)
    print(cnts)
    return min(cnts[max(cnts)])


if __name__ == '__main__':
    print(electionWinner([
        "Alex",
        "Michael",
        "Harry",
        "Dave",
        "Michael",
        "Victor",
        "Harry",
        "Alex",
        "Mary",
        "Mary",
    ]))
