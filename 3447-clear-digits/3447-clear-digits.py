class Solution(object):
    def clearDigits(self, s):
        """
        :type s: str
        :rtype: str
        """
        res=[]
        def isdigit(c):
            return ord("0") <= ord(c)<=ord("9")

        for i in range(len(s)):
            if isdigit(s[i]):
                res.pop()
            else:
                res.append(s[i])
        
        return "".join(res)