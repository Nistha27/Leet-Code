class Solution(object):
    def numberOfPowerfulInt(self, start, finish, limit, s):
        """
        :type start: int
        :type finish: int
        :type limit: int
        :type s: str
        :rtype: int
        """
        def calculate(x, s, limit):
            if len(x) < len(s):
                return 0
            if len(x) == len(s):
                return 1 if x >= s else 0

            suffix = x[len(x) - len(s) :]
            count = 0
            pre_len = len(x) - len(s)

            for i in range(pre_len):
                if limit < int(x[i]):
                    count += (limit + 1) ** (pre_len - i)
                    return count
                count += int(x[i]) * (limit + 1) ** (pre_len - 1 - i)

            if suffix >= s:
                count += 1

            return count

        start_ = str(start - 1)
        finish_ = str(finish)
        return calculate(finish_, s, limit) - calculate(start_, s, limit)

        