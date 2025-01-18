class Solution(object):
    def minCost(self, arr, brr, k):
        """
        :type arr: List[int]
        :type brr: List[int]
        :type k: int
        :rtype: int
        """
        no_rearrange_cost = sum(abs(a - b) for a, b in zip(arr, brr))
        
        arr_sorted = sorted(arr)
        brr_sorted = sorted(brr)
        rearrange_cost = k + sum(abs(a - b) for a, b in zip(arr_sorted, brr_sorted))
        
        return min(no_rearrange_cost, rearrange_cost)