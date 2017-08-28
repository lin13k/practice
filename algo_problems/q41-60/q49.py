class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        dic = {}
        for i in range(len(strs)):
            sortedValue = tuple(sorted(strs[i]))
            if sortedValue in dic:
                dic[sortedValue].append(strs[i])
            else:
                dic[sortedValue] = [strs[i]]

        return [dic[i] for i in dic]
