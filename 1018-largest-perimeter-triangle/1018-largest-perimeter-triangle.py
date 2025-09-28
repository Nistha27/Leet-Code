class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        #triangle cond a+b>c,c+b>a,c+a>a
        nums.sort()
        for i in range(len(nums)-3,-1,-1):
            if nums[i]+nums[i+1]>nums[i+2]:
                return nums[i]+nums[i+1]+nums[i+2]
        return 0
