class Solution(object):
    def maxScore(self, s):
        """
        :type s: str
        :rtype: int
        """
        zero=0 # no of zeroes in the left substring
        ones=s.count("1")
        result=0
        for i in range(len(s)-1): # -1 because there should be non empty right substring
            if s[i]=="0":
                zero+=1 
            else:
                ones-=1 # decreasing the no of 1's as it is encountered in right substring
            result=max(result,zero+ones)
        return result
