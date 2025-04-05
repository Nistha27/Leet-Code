class Solution(object):
    def subsetXORSum(self, nums):
        def dfs(i,total):

            if i==len(nums):
                return total
            return dfs(i+1,total^nums[i]) + dfs(i+1,total)  #include nums[i] + #not include nums[i]
        return dfs(0,0)

        
        