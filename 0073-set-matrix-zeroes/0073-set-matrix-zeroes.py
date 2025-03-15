class Solution(object):
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        m=len(matrix)
        n=len(matrix[0])
        def markcol(matrix,i,n):
            for j in range(n):
                if matrix[i][j]!=0:
                    matrix[i][j]="#"
        def markrow(matrix,j,m):
            for i in range(m):
                if matrix[i][j]!=0:
                    matrix[i][j]="#"

        for i in range(m):
            for j in range(n):
                if matrix[i][j]==0:
                    markrow(matrix,j,m)
                    markcol(matrix,i,n)

        for i in range(m):
            for j in range(n):
                if matrix[i][j]=="#":
                    matrix[i][j]=0       