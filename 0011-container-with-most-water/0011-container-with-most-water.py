class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        n=len(height)
        i=0
        j=n-1
        max_area=0
        while i<j:
            max_area=max(max_area,(j-i)*min(height[j],height[i]))
            if height[i]<height[j]:
                i+=1
            else:
                j-=1

        return max_area

        