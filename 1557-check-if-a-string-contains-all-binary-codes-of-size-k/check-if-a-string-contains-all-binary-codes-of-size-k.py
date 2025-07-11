class Solution:
    def hasAllCodes(self, s: str, k: int) -> bool:
        need = 1 << k
        # 1. find all unique binary codes from s of length k

        codeset = set()

        for i in range(len(s)-k + 1):
            tmp = s[i:i+k]
            codeset.add(tmp)
        
        return need == len(codeset)