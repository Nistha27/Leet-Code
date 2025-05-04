class Solution(object):
    def numEquivDominoPairs(self, dominoes):
        count=0
        '''for i in range(len(dominoes)):
            a,b=dominoes[i][0],dominoes[i][1]
            for j in range(i+1,len(dominoes)):
                c,d=dominoes[j][0],dominoes[j][1]
                if (a==c and b==d) or (a==d and b==c):
                    count+=1
        return count'''
        ret=0
        num=[0]*100
        for x,y in dominoes :
            val=x*10+y if x<=y else y*10+x
            ret=ret+num[val]
            num[val]+=1
        return ret
