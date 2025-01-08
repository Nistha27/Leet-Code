class Solution(object):
    def largestAltitude(self, gain):
        """
        :type gain: List[int]
        :rtype: int
        """
        res=[0]*(len(gain)+1)
        for i in range(1,len(gain)+1):
            res[i]=res[i-1]+gain[i-1]
        return (max(res))