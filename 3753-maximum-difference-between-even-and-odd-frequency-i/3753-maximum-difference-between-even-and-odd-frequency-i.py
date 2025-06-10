class Solution(object):
    def maxDifference(self, s):
        """
        :type s: str
        :rtype: int
        """
        count_alpha=Counter(s)
        odd_freq=[value for value in count_alpha.values() if value%2!=0]
        even_freq=[value for value in count_alpha.values() if value%2==0]

        if not odd_freq or not even_freq:
            return -1
        return max(odd_freq)-min(even_freq)
            