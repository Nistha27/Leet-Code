class Solution(object):
    def setZeroes(self, matrix):
        #Brute Force
        n=len(matrix)
        m=len(matrix[0])
        '''def markcol(matrix,i,n):
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
                    matrix[i][j]=0'''

        #Better Approach

        row=[0]*n
        col=[0]*m

        for i in range(n):
            for j in range(m):
                if matrix[i][j]==0:
                    row[i]=1
                    col[j]=1

        for i in range(n):
            for j in range(m):
                if row[i] or col[j]:
                    matrix[i][j]=0
    



    