class Solution(object):
    def maximumTripletValue(self, nums):
        #Brute Force
        '''res=[]
        for i  in range(len(nums)):
            for j in range(i+1,len(nums)):
                for k in range(j+1,len(nums)):
                    sum=(nums[i]-nums[j])*nums[k]
                    res.append(sum)
        if max(res)<0:
            return 0
        else:
            return max(res)'''

        #O(n^3)->O(n^2)
        N=len(nums)
        res=0
        left=nums[0]
        for j in range(1,N):
            if nums[j] >left:
                left=nums[j]
                continue
            for k in range(j+1,N):
                res = max(res,(left-nums[j])*nums[k])
                
        return res