class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        str_split=s.split()
        str_split=str_split[::-1]
        res=''
        for i in range(len(str_split)):
            res+=str_split[i]
            if i!=(len(str_split)-1):
                res+=' '
            else:
                continue
            print(res)
        return res
        