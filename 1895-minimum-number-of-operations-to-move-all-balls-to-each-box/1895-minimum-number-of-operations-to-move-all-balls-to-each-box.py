class Solution(object):
    def minOperations(self, boxes):
        """
        :type boxes: str
        :rtype: List[int]
        """
        #Brute Force
        '''res=[0]*len(boxes)
        for i in range(len(boxes)):
            for j in range(len(boxes)):
                if boxes[j]=="1":
                    res[i]+=abs(j-i)
        return res'''

        #Optimal Solution
        res=[0]*len(boxes)

        balls,moves=0,0
        for i in range(len(boxes)):
            res[i]=balls+moves
            moves=moves+balls
            balls+=int(boxes[i])

        balls,moves=0,0
        for i in reversed(range(len(boxes))):
            res[i]+=balls+moves
            moves=moves+balls
            balls+=int(boxes[i])
        return res