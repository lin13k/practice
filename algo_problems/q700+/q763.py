class Solution:
    def partitionLabels(self, S):
        """
        :type S: str
        :rtype: List[int]
        """
        st = set()
        startList = [' ' for i in range(len(S))]
        for i, c in enumerate(S):
            if c not in st:
                st.add(c)
                startList[i] = c

        st = set()
        endList = [' ' for i in range(len(S))]
        for i, c in enumerate(S[::-1]):
            if c not in st:
                st.add(c)
                endList[i] = c
        endList = endList[::-1]

        cnt = 0
        preIndex = 0
        result = []
        for i in range(len(S)):
            if startList[i] != ' ':
                cnt += 1
            if endList[i] != ' ':
                cnt -= 1
            if cnt == 0:
                result.append(i + 1 - preIndex)
                preIndex = i + 1
        if preIndex < len(S):
            result.append(len(S) - preIndex)
        return result


if __name__ == '__main__':
    print(Solution().partitionLabels('ababcbacadefegdehijhklij'))
