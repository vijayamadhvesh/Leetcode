class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        p_count = Counter(p)
        d = Counter()
        n, k = len(s), len(p)
        res = []
        
        for i in range(n):
            d[s[i]] += 1

            if i >= k:
                d[s[i-k]] -= 1
                if d[s[i-k]] == 0:
                    del d[s[i-k]]
            
            if d == p_count:
                res.append(i-k+1)

        print(res)
        return res