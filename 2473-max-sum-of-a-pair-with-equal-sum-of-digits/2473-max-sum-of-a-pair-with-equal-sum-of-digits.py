class Solution(object):
    def maximumSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        digit_sum_map = defaultdict(list)
        max_sum = -1

        # Group numbers by their digit sum
        for num in nums:
            digit_sum = sum(int(digit) for digit in str(num))
            digit_sum_map[digit_sum].append(num)

        # Find the maximum sum among pairs with the same digit sum
        for values in digit_sum_map.values():
            if len(values) > 1:
                values.sort(reverse=True)  # Sort descending
                max_sum = max(max_sum, values[0] + values[1])  # Take the top two numbers

        return max_sum
        