class Solution(object):
    def minOperations(self, boxes):
        """
        :type boxes: str
        :rtype: List[int]
        """
        res=[0]*len(boxes)
        for i in range(len(boxes)):
            for j in range(len(boxes)):
                if boxes[j]=="1":
                    res[i]+=abs(j-i)
        return res