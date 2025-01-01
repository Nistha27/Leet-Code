class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        m=len(matrix)
        n=len(matrix[0])
        left, right = 0, m*n-1
        while left<=right:
            mid =  left + (right-left)//2
            mid_elem = matrix[mid//n][mid%n]
            if mid_elem == target:
                return True
            elif mid_elem < target:
                left = mid+1
            else:
                right=mid-1
        return False