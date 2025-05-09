
def comb(n, k, MOD=None):
    if k < 0 or k > n:
        return 0
    res = 1
    for i in range(1, k + 1):
        res *= n - i + 1
        res //= i
        if MOD:
            res %= MOD
    return res if not MOD else res % MOD

class Solution:
    def countBalancedPermutations(self, num):
        MOD = 10**9 + 7
        tot, n = 0, len(num)
        cnt = [0] * 10
        for ch in num:
            d = int(ch)
            cnt[d] += 1
            tot += d
        if tot % 2 != 0:
            return 0

        target = tot // 2
        max_odd = (n + 1) // 2
        f = [[0] * (max_odd + 1) for _ in range(target + 1)]
        f[0][0] = 1
        psum = tot_sum = 0
        for i in range(10):
            psum += cnt[i]
            tot_sum += i * cnt[i]
            for odd_cnt in range(min(psum, max_odd), max(0, psum - (n - max_odd)) - 1, -1):
                even_cnt = psum - odd_cnt
                for curr in range(min(tot_sum, target), max(0, tot_sum - target) - 1, -1):
                    res = 0
                    for j in range(max(0, cnt[i] - even_cnt), min(cnt[i], odd_cnt) + 1):
                        if i * j > curr:
                            break
                        ways = (comb(odd_cnt, j) * comb(even_cnt, cnt[i] - j)) % MOD
                        res = (res + ways * f[curr - i * j][odd_cnt - j] % MOD) % MOD
                    f[curr][odd_cnt] = res % MOD

        return f[target][max_odd]
