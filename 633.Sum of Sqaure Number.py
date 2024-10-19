'''Given a non-negative integer c, decide whether there're two integers a and b such that a^2 + b^2 = c.'''

'''
Example 1:
Input: c = 5
Output: true
Explanation: 1 * 1 + 2 * 2 = 5

Example 2:
Input: c = 3
Output: false
 '''

'''def square(num):
    if(num==1):
        return True
    for i in range(num):
        for j in range(1,num):
            if((i**2+j**2)==num):
                return True
    return False
    
a=square(1)
print(a)'''

'''class Solution(object):
    def judgeSquareSum(self, c):
        self.c=c
        for i in range(c):
            for j in range(1,c):
                print(i)
                print(j)
                if((i**2+j**2)==c):
                    return True
        return False'''
    
'''p=Solution()
a=p.judgeSquareSum(1)
print(a)'''
class Solution(object):
    def judgeSquareSum(self, c):
        self.c=c
        for i in range(int(c**0.5)+1):
            b=c-i**2

            if(int(b**0.5)==b**0.5):
                return True
        return False
    
'''class Solution(object):
    def judgeSquareSum(self, c):
        """
        :type c: int
        :rtype: bool
        """
        first = 0
        last = int(c ** 0.5)

        while first <= last: 
            total = first ** 2 + last ** 2
            if total == c:
                return True
            elif total > c:
                last -= 1
            else: 
                first += 1
        return False'''
# cook your dish here



                                 
                          