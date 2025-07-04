class Solution(object):
    def kthCharacter(self, k, operations):
        '''word='a'
        for i in range(len(operations)):
            if operations[i]==0:
                word+=word
            else:
                for j in range(len(word)):
                    word+=chr(ord(word[j])+1)
        return word[k-1]'''
        ans = 0
        while k != 1:
            t = k.bit_length() - 1
            if (1 << t) == k:
                t -= 1
            k -= 1 << t
            if operations[t]:
                ans += 1
        return chr(ord("a") + (ans % 26))
        

