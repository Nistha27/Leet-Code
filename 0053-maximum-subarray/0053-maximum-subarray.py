class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """    
        n=len(nums)
        sum1=0
        max1=float("-inf")
        for i in range(n):
            sum1=sum1+nums[i]
            max1=max(sum1,max1)
            if sum1<0:
                sum1=0
        return max1