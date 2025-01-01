class Solution(object):
    def maxScore(self, s):
        """
        :type s: str
        :rtype: int
        """
        zero=0
        ones=s.count("1")
        result=0
        for i in range(len(s)-1):
            if s[i]=="0":
                zero+=1
            else:
                ones-=1
            result=max(result,zero+ones)
        return result
