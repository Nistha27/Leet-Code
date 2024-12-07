class Solution(object):
    def twoSum(self, nums, target):
        # Create a dictionary to store the complement and its index
        seen = {}
        for i, num in enumerate(nums):
            complement = target - num
            if complement in seen:
                return [seen[complement], i]  # Return the indices
            seen[num] = i  # Store the current number with its index
        return [] 
