class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n=len(nums)
        curr_sum=nums[0]
        maxi=nums[0]
        for i in range(1,n):
            curr_sum=max(nums[i],curr_sum+nums[i])
            if curr_sum>maxi :
                maxi=curr_sum
        return maxi

        