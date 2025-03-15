class Solution(object):
    def setZeroes(self, matrix):
        #Brute Force
        #n=len(matrix)
        #m=len(matrix[0])
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

        '''row=[0]*n
        col=[0]*m

        for i in range(n):
            for j in range(m):
                if matrix[i][j]==0:
                    row[i]=1
                    col[j]=1

        for i in range(n):
            for j in range(m):
                if row[i] or col[j]:
                    matrix[i][j]=0'''

        #Optimal Approach
        rows = set()
        cols = set()
        n, m = len(matrix), len(matrix[0])
        # Find first rows and cols
        for i in range(n):
            for j in range(m):
                if matrix[i][j] == 0:
                    rows.add(i)
                    cols.add(j)
        # Set rows to zero
        for i in rows:
            for j in range(m):
                matrix[i][j] = 0
        # Set cols to zero
        for i in range(n):
            for j in cols:
                matrix[i][j] = 0
    



    