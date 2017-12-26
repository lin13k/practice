class Solution:
    def simplifyPath(self, path):
        """
        :type path: str
        :rtype: str
        """
        folderList = path.split('/')
        stack = []
        for i in folderList:
            if i == '.' or i == '':
                continue
            if i == '..':
                if len(stack) != 0:
                    stack.pop()
            else:
                stack.append(i)

        if len(stack) == 0:
            return '/'
        else:
            return '/' + '/'.join(stack)


if __name__ == '__main__':
    print(Solution().simplifyPath('/'))
    print(Solution().simplifyPath('/abc/def/hijk/..'))
    print(Solution().simplifyPath('/..'))
    print(Solution().simplifyPath('/../abc/abc/..'))
