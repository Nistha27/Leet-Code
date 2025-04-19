class Solution(object):
    def countFairPairs(self, nums, lower, upper):
        
        #2For Loops- O(n^2)
        '''count=0
        N=len(nums)
        for i in range(N):
            for j in range(i+1,N):
                if nums[i]+nums[j]>=lower and nums[i]+nums[j]<=upper:
                    count+=1
        return count'''


        #Binary Search - O(nlogn)
        
        def lower_bound(nums,low,high,elem):
            while low<=high:
                mid= low + ((high-low)//2)
                if nums[mid]>=elem:
                    high=mid-1
                else:
                    low=mid+1
            return low
        nums.sort()
        ans=0
        for i in range(len(nums)):
            low=lower_bound(nums,i+1,len(nums)-1,lower-nums[i])
            high=lower_bound(nums,i+1,len(nums)-1,upper-nums[i]+1)

            ans+=high-low

        return ans

        


