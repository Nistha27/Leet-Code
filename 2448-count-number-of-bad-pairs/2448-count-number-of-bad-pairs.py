class Solution(object):
    def countBadPairs(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        good_pairs=0
        total_pairs=0
        count=defaultdict(int)
        for i in range(len(nums)):
            total_pairs+=i
            good_pairs+=count[nums[i]-i]
            count[nums[i]-i]+=1
        return total_pairs-good_pairs