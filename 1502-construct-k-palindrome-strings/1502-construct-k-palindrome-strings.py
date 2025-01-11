class Solution(object):
    def canConstruct(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: bool
        """
        if k>len(s):
            return False
        count=Counter(s)
        odd=0
        for cnt in count.values():
            odd+= cnt % 2
        return odd<=k