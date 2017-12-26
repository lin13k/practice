class Solution:
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """

        # give the n*m matrix
        # scan the matrix first for the zero
        #
        n = len(matrix)
        if n == 0:
            return
        m = len(matrix[0])
        if m == 0:
            return

        zero_in_first_column = False
        for i in range(n):
            if matrix[i][0] == 0:
                zero_in_first_column = True

        zero_in_first_row = False
        for i in range(m):
            if matrix[0][i] == 0:
                zero_in_first_row = True

        for i in range(1, n):
            for j in range(1, m):
                if matrix[i][j] == 0:
                    matrix[0][j] = 0
                    matrix[i][0] = 0

        # set the matrix with the information in the first column and fist row
        for i in range(1, n):
            for j in range(1, m):
                if matrix[0][j] == 0 or matrix[i][0] == 0:
                    matrix[i][j] = 0

        if matrix[0][0] == 0:
            for i in range(n):
                matrix[i][0] = 0
            for i in range(m):
                matrix[0][i] = 0
        else:
            if zero_in_first_column:
                for i in range(n):
                    matrix[i][0] = 0
            if zero_in_first_row:
                for i in range(m):
                    matrix[0][i] = 0
            