class Solution(object):
    def gridGame(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        n = len(grid[0])
        # Create prefix sums for both rows
        preRow1, preRow2 = grid[0][:], grid[1][:]

        for i in range(1, n):
            preRow1[i] += preRow1[i-1]
            preRow2[i] += preRow2[i-1]

        res = float("inf")
        # Calculate the maximum score for the second robot
        for i in range(n):
            top = preRow1[-1] - preRow1[i]  # Remaining points in the first row
            bottom = preRow2[i-1] if i > 0 else 0  # Points collected by the second robot
            secondRobot = max(top, bottom)
            res = min(res, secondRobot)

        return res
