class Solution:
    MOD = 10**9 + 7

    def idealArrays(self, n, maxValue):
        count = [[0] * 10005 for _ in range(15)]
        prefix_sum = [[0] * 10005 for _ in range(15)]
        options = [0] * 15

        def countUniqueSequences(curr, idx, maxValue):
            options[idx] += 1
            j = 2
            while curr * j <= maxValue:
                countUniqueSequences(curr * j, idx + 1, maxValue)
                j += 1

        # Pre-fill 1st row
        for i in range(1, 10001):
            count[1][i] = 1
            prefix_sum[1][i] = i

        # Fill the count table
        for i in range(2, 15):
            for j in range(i, 10001):
                count[i][j] = prefix_sum[i - 1][j - 1]
                prefix_sum[i][j] = (count[i][j] + prefix_sum[i][j - 1]) % self.MOD
                count[i][j] %= self.MOD

        # Calculate options
        for i in range(1, maxValue + 1):
            countUniqueSequences(i, 1, maxValue)

        # Count total ideal arrays
        ans = 0
        for i in range(1, 15):
            ways = (count[i][n] * options[i]) % self.MOD
            ans = (ans + ways) % self.MOD
        return ans