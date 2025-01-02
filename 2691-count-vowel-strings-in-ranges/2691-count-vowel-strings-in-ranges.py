class Solution(object):
    def vowelStrings(self, words, queries):
        """
        :type words: List[str]
        :type queries: List[List[int]]
        :rtype: List[int]
        """
        #taking in all the vowels in the alphabet as set
        vowel_set = set("aeiou")
        #taking in a array to show the count of words that start and end with vowels 
        #from the begining taking an offset 
        prefix_cnt = [0]*(len(words)+1)
        #taking a prev because diff between then would give us the res 
        #as count is from 0 index position
        prev=0
        for i,w in enumerate(words):
            if w[0] in vowel_set and w[-1] in vowel_set:
                prev+=1
            prefix_cnt[i+1]=prev
            
        res=[0]*len(queries)
        for i,q in enumerate(queries):
            l,r=q
            res[i]=prefix_cnt[r+1]-prefix_cnt[l]

        return res
        