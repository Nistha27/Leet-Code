class Solution(object):
    def maximumTripletValue(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        res=[]
        for i  in range(len(nums)):
            for j in range(i+1,len(nums)):
                for k in range(j+1,len(nums)):
                    sum=(nums[i]-nums[j])*nums[k]
                    res.append(sum)
        if max(res)<0:
            return 0
        else:
            return max(res)