class Solution(object):
    def countSymmetricIntegers(self, low, high):
        """
        :type low: int
        :type high: int
        :rtype: int
        """
        
        count = 0
        for i in range(low, high+1):
            sum_ = 0
            sum__ = 0
            num_list = list(str(i))
            n = len(num_list) // 2  # Integer division

            for j in num_list[:n]:
                sum_ += int(j)
            for k in num_list[n:]:
                sum__ += int(k)

            if sum_ == sum__:
                count += 1
                print(i)
        return count

        