class Solution(object):
    def findThePrefixCommonArray(self, A, B):
        """
        :type A: List[int]
        :type B: List[int]
        :rtype: List[int]
        """
        n = len(A)
        C = [0] * n  # Initialize the prefix common array
        seen_A = set()  # Track elements seen in A
        seen_B = set()  # Track elements seen in B
        common_count = 0  # Counter for common elements

        for i in range(n):
            # Add current elements to their respective sets
            seen_A.add(A[i])
            seen_B.add(B[i])
            
            # Check if the current elements are common
            if A[i] in seen_B:
                common_count += 1
            if B[i] in seen_A and A[i] != B[i]:
                common_count += 1
            
            # Update the prefix common array
            C[i] = common_count

        return C

        