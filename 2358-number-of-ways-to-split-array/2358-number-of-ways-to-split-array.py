class Solution(object):
    def waysToSplitArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        #Brute Force Approach
        '''count=0
        for i in range(len(nums)-1):
            if sum(nums[:i+1])>=sum(nums[i+1:]):
                count+=1
        return count'''

        # Optimized Approach
        right=sum(nums) #O(n)
        left=0
        res=0
        #taking right as total sum and subtracting it by left after every single iterartion 
        #checking the condition
        for i in range(len(nums)-1):
            left+=nums[i]
            right-=nums[i]

            if left>=right :
                res+=1
        return res
        