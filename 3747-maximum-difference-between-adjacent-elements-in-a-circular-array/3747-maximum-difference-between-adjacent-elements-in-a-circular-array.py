class Solution(object):
    def maxAdjacentDistance(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) < 2:
            return 0
    
        max_diff = 0
        n = len(nums)
    
        for i in range(n):
            diff = abs(nums[i] - nums[(i + 1) % n])
            max_diff = max(max_diff, diff)
        
        return max_diff    