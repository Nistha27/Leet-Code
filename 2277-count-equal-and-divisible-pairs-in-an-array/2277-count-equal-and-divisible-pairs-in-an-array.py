class Solution(object):
    def countPairs(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        count=0
        N=len(nums)
        for i in range(N-1):
            for  j in range(i+1,N):
                if (i*j)%k==0 and nums[i]==nums[j]:
                    count+=1 
        return count