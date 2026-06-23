class Solution:
    def isPalindrome(self, x: int) -> bool:
        dup=x
        rev_no=0
        while(x>0):
            l_d=x%10
            x//=10
            rev_no=rev_no*10+l_d
        return rev_no==dup