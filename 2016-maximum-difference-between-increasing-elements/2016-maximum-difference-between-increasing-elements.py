class Solution:
    def maximumDifference(self, nums: List[int]) -> int:
        n=len(nums)
        # Variable to store the minimum 
        # value found so far. 
        mini=nums[0]
        ans=-1
        for i in range(1,n):
        # If arr[i] is less than equal 
        # to minimum value, update mini.
            if nums[i]<= mini:
                mini=nums[i]
            else:
                ans=max(ans,nums[i]-mini)
        return ans

