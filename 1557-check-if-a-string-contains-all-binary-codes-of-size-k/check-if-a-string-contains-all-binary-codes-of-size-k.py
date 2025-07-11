class Solution:
    def hasAllCodes(self, s: str, k: int) -> bool:
        seen = set()
        total = 1 << k  # This is 2^k

        for i in range(len(s) - k + 1):
            substring = s[i:i+k]
            seen.add(substring)
            if len(seen) == total:
                return True  # Early exit

        return len(seen) == total