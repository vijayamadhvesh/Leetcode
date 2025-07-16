class Solution:
    def maxProduct(self, s: str) -> int:
        
        @cache
        def lps(mask): 
            """Return length of longest palindromic sequence."""
            if not mask: return 0
            if not mask & (mask-1): return 1
            lo = int(log2(mask & ~(mask-1))) # least significant set bit
            hi = int(log2(mask)) # most significant set bit 
            if s[lo] == s[hi]: return 2 + lps(mask^(1<<lo)^(1<<hi))
            return max(lps(mask^(1<<lo)), lps(mask^(1<<hi)))
        
        ans = 0
        for mask in range(1 << len(s)): 
            comp = (1 << len(s)) - 1 ^ mask
            ans = max(ans, lps(mask) * lps(comp))
        return ans 