class Solution(object):
    def stringMatching(self, words):
        """
        :type words: List[str]
        :rtype: List[str]
        """
        res=[]
        for i in range(len(words)):
            for j in range(len(words)):
                if words[i]==words[j]:
                    continue
                elif words[i] in words[j] and words[i] not in res:
                    res.append(words[i])
        return res
