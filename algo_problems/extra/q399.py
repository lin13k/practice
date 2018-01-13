import collections

class Solution:
    def calcEquation(self, equations, values, queries):
        """
        :type equations: List[List[str]]
        :type values: List[float]
        :type queries: List[List[str]]
        :rtype: List[float]
        """
        d = collections.defaultdict(dict)
        for (src, dst), value in zip(equations, values):
            print(src, dst, value)
            d[src][src] = 1.0
            d[dst][dst] = 1.0
            d[src][dst] = value
            d[dst][src] = 1.0 / value
        for i in d:
            for j in d[i]:
                for k in d[i]:
                    d[j][k] = d[j][i] * d[i][k]
        result = []
        for (srcq, dstq) in queries:
            if dstq in d[srcq]:
                result.append(d[srcq][dstq])
            else:
                result.append(-1)

        return result
            