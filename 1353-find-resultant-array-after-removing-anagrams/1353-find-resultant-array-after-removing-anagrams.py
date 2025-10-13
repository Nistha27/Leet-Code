class Solution(object):
    def removeAnagrams(self, words):
        n = len(words)
        freq = [Counter(w) for w in words]
        print(freq)
        ans = [words[0]]
        for i in range(1, n):
            if freq[i] != freq[i - 1]:
                ans.append(words[i])
        return ans