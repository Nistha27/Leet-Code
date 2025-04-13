class Solution(object):
    def countGoodNumbers(self, n):
        #Mathematical Solution
        '''
        mod=(10**9+7)
        if n%2==0:
            return ((20**(n/2)))%mod
        else:
            return ((20**(n/2))*5)%mod '''   
        #Optimal: Recursion
        mod=10**9+7
        def multiply(x,y):
            result=1
            mul=x
            while(y>0):
                if y%2==1:
                    result=result*mul%mod
                mul=mul*mul%mod
                y//=2
            return result

        return multiply(5,(n+1)//2)*multiply(4,n//2)%mod
    
