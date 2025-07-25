class Solution:
    def maxSum(self, nums):
        positiveNumsSet = set([num for num in nums if num > 0])
        return max(nums) if len(positiveNumsSet) == 0 else sum(positiveNumsSet)