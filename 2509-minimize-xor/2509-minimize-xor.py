class Solution(object):
    def minimizeXor(self, num1, num2):
        """
        :type num1: int
        :type num2: int
        :rtype: int
        """
        def count_bits(n):
            res=0
            while n>0:
                res+=1 & n
                n=n>>1
            return res
        cnt1,cnt2=count_bits(num1),count_bits(num2)
        x=num1
        i=0

        while cnt1!= cnt2:
            if cnt2<cnt1 and x &(1<<i):
                cnt1-=1
                x=x^(1<<i)
            if cnt1 < cnt2 and x & (1<<i)==0:
                cnt1+=1
                x=x | (1<<i)
            i+=1
        return x