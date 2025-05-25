from collections import Counter
class Solution:
    def longestPalindrome(self, words):
        freq = Counter(words)
        length = 0
        central = False
        for word in freq:
            rev = word[::-1]
            if word == rev:
                pair_count = freq[word] // 2
                length += pair_count * 4  
                if freq[word] % 2 == 1:
                    central = True  
            elif word < rev:
                pair_count = min(freq[word], freq[rev])
                length += pair_count * 4
        if central:
            length += 2  
        return length