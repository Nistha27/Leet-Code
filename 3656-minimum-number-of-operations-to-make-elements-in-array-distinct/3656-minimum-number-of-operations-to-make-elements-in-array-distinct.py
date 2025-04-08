class Solution(object):
    def minimumOperations(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        def check_unique(start):
            seen = set()
            for num in nums[start:]:
                if num in seen:
                    return False
                seen.add(num)
            return True

        ans = 0
        for i in range(0, len(nums), 3):
            if check_unique(i):
                return ans
            ans += 1
        return ans
        
        