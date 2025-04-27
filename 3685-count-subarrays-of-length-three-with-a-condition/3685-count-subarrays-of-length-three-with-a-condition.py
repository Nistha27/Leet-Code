class Solution(object):
    def countSubarrays(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        count=0
        n= len(nums)
        for i in range(1,n-1):
            if nums[i]==(nums[i-1]+nums[i+1])*2 :
                count+=1
        return count

        