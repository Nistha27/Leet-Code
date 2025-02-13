class Solution(object):
    def minOperations(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        heapq.heapify(nums)  # Convert nums into a min-heap
        operations = 0

        while len(nums) > 1 and nums[0] < k:
            x = heapq.heappop(nums)  # Smallest element
            y = heapq.heappop(nums)  # Second smallest element
            new_val = min(x, y) * 2 + max(x, y)
            heapq.heappush(nums, new_val)  # Insert the new value
            operations += 1

        return operations if nums[0] >= k else -1  # Return -1 if we can't reach k