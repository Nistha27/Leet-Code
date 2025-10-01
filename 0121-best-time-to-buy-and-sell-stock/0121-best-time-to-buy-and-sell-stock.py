class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_p=0
        min_p=float('inf')
        for price in prices:
            min_p=min(min_p,price)
            max_p=max(max_p,price-min_p)
        return max_p