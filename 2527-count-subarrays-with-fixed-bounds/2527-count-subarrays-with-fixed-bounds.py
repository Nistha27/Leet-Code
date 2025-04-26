class Solution(object):
    def countSubarrays(self, nums, minK, maxK):
        """
        :type nums: List[int]
        :type minK: int
        :type maxK: int
        :rtype: int
        """
        ans=0
        badi=-1
        mini=-1
        maxi=-1
        n=len(nums)

        for i in range(n):
            if nums[i] < minK or nums[i] > maxK :
                badi=i
            if nums[i]==minK :
                mini=i
            if nums[i]==maxK :
                maxi=i
            ans+= max(0,min(mini,maxi)-badi)

        return ans

        