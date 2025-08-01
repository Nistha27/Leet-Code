class Solution:
    def generate(self, numRows):
        pascal = []

        for i in range(numRows):
            row = [1] * (i + 1) 
            for j in range(1, i):
                row[j] = pascal[i - 1][j - 1] + pascal[i - 1][j]
            pascal.append(row)

        return pascal