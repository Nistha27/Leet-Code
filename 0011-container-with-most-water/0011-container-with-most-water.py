class Solution:
    def maxArea(self, height: List[int]) -> int:
        "BRUTE FORCE"
        '''n=len(height)
        area=0
        for i in range(n):
            for j in range(i+1,n):
                if height[i]>height[j]:
                    area=max(area,height[j]*(j-i))
                elif height[i]<height[j]:
                    area=max(area,height[i]*(j-i))
                else:
                    area=max(area,height[i]*(j-i))
        return area'''

        "OPTIMIZED SOLUTION"
        n=len(height)
        max_area=0
        left=0
        right=n-1
        while left<right:
            max_area=max(max_area,(right-left)*min(height[left],height[right]))

            if height[left]<height[right]:
                left+=1
            else:
                right-=1
        return max_area