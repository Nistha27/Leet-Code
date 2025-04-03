class Solution(object):
    def maximumTripletValue(self, nums):

        #o(n^2)->O(n)
        '''res=0
        N=len(nums)
        left=nums[0]
        for j in range(1,N):
            if left<nums[j]:
                left=nums[j]
                continue
            for k in range(j+1,N):
                res=max((left-nums[j])*nums[k],res)
        return res '''
        
        N=len(nums)
        prefix_max=nums[0]
        max_diff=0
        res=0
        for k in range(1,N):
            res=max(res,max_diff*nums[k])
            prefix_max=max(prefix_max,nums[k])
            max_diff=max(max_diff,prefix_max-nums[k])
        return res