class Solution:
    def kthCharacter(self, k: int) -> str:
        res = 'a'

        while len(res)<k:
            n = len(res)
            for i in range(n):
                res += chr(ord(res[i])+1)
        return res[k-1]