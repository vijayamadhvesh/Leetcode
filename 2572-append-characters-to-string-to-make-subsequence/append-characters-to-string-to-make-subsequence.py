class Solution:
    def appendCharacters(self, s: str, t: str) -> int:
        i = 0
        n = len(t)

        for ch in s:
            if i<n and t[i] == ch:
                i += 1
            
        return n - i