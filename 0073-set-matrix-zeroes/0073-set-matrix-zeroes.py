from typing import List

class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        m = len(matrix)        # number of rows
        n = len(matrix[0])     # number of columns
        
        row = [0] * m
        col = [0] * n

        # Step 1: Mark rows and cols that should be zero
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 0:
                    row[i] = 1
                    col[j] = 1

        # Step 2: Set cells to zero if in marked row/col
        for i in range(m):
            for j in range(n):
                if row[i] or col[j]:
                    matrix[i][j] = 0
