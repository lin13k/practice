from collections import defaultdict, deque


def closest(s, queries):
    # Write your code here
    n = len(s)
    m = [-1 for i in range(n)]
    d = defaultdict(lambda: deque([-1, -1], 2))

    for i, c in enumerate(s):
        d[c].append(i)
        if d[c][0] == -1:
            m[i] = -1
        else:
            if m[d[c][0]] == -1:
                m[d[c][0]] = d[c][1]
                m[i] = d[c][0]
            else:
                if d[c][0] - m[d[c][0]] > d[c][1] - d[c][0]:
                    m[d[c][0]] = d[c][1]
                m[i] = d[c][0]
    return [m[q] for q in queries]


if __name__ == '__main__':
    print(closest('hackerrank', [4, 1, 6, 8]))
