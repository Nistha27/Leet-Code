class Solution(object):
    def smallestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """

        freq = Counter(s)
        # Step 1: Check how many characters have odd frequency
        odd_chars = [char for char in freq if freq[char] % 2 != 0]
        if len(odd_chars) > 1:
            return ""  # Cannot form a palindrome
    
        # Step 2: Build the half part of the palindrome
        half = []
        middle = ""
        
        for char in sorted(freq.keys()):
            count = freq[char]
            if count % 2 != 0:
                middle = char
            half.append(char * (count // 2))
        
        half_str = ''.join(half)
        return half_str + middle + half_str[::-1]

            


                
            