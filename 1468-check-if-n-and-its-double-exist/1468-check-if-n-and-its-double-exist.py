class Solution(object):
    def checkIfExist(self, arr):
        """
        :type arr: List[int]
        :rtype: bool
        """
        for i in range(len(arr)):
            for j in range(len(arr)):
                # Step 2: Check the conditions
                if i != j and arr[i] == 2 * arr[j]:
                    return True
        # No valid pair found
        return False
        