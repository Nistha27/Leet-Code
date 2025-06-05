class Solution(object):
    def smallestEquivalentString(self, s1, s2, baseStr):
        parent = list(range(26))  # For letters 'a' to 'z'

        def find(x):
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]

        def union(x, y):
            px = find(x)
            py = find(y)
            if px != py:
                # Always keep the lexicographically smaller as the parent
                if px < py:
                    parent[py] = px
                else:
                    parent[px] = py

        # Union the characters from s1 and s2
        for a, b in zip(s1, s2):
            union(ord(a) - ord('a'), ord(b) - ord('a'))

        # Build the result for baseStr
        result = []
        for c in baseStr:
            smallest_char = chr(find(ord(c) - ord('a')) + ord('a'))
            result.append(smallest_char)

        return ''.join(result)

        