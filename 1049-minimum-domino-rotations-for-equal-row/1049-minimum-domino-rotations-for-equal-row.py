class Solution(object):
    def minDominoRotations(self, tops, bottoms):
        """
        :type tops: List[int]
        :type bottoms: List[int]
        :rtype: int
        """
        for target in [tops[0],bottoms[0]]:
            missT,missB=0,0
            for i,pair in enumerate(zip(tops,bottoms)):
                top,bottom=pair
                #top == t1 or  bottom==t2
                if not(top==target or bottom==target):
                    break
                if top!=target:
                    missT+=1
                if bottom!=target:
                    missB+=1
                if i==len(tops)-1:
                    return min(missT,missB)
        return -1
        
        