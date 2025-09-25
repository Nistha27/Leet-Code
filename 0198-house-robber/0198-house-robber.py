def solveUtil(n,nums,dp):
        if dp[n]!=-1:
            return dp[n]

        if n==0:
            return nums[n]
        if n<0:
            return 0
        
        pick=nums[n]+solveUtil(n-2,nums,dp)
        not_pick=0+solveUtil(n-1,nums,dp)

        dp[n]=max(pick,not_pick)
        return dp[n]

class Solution(object): 
    def rob(self, nums):
        n=len(nums)
        dp=[-1 for i in range(n)]
        return solveUtil(n-1,nums,dp)
    