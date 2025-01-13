class Solution(object):
    def minimumLength(self, s):
        """
        :type s: str
        :rtype: int
        """

        count_char=Counter(s)
        ans=0
        for values in count_char.values():
            while values >= 3 :
                values-=2
            ans+=values
        

        return ans