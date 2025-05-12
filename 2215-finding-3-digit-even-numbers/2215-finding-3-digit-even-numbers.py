from itertools import permutations

class Solution(object):
    def findEvenNumbers(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        result = set()
        for perm in permutations(digits, 3):
            if perm[0] == 0:
                continue  # Skip numbers starting with 0
            if perm[2] % 2 != 0:
                continue  # Last digit must be even
            num = perm[0] * 100 + perm[1] * 10 + perm[2]
            result.add(num)
        return sorted(result)
