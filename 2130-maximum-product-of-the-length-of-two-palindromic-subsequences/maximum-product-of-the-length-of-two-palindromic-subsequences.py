class Solution:
    def maxProduct(self, s: str) -> int:
        n = len(s)
        palindromes = []

        def is_palindrome(sub):
            return sub == sub[::-1]

        # Generate all subsequences via bitmask
        for mask in range(1, 1 << n):
            sub = ''
            for i in range(n):
                if mask & (1 << i):
                    sub += s[i]
            if is_palindrome(sub):
                palindromes.append((mask, len(sub)))

        max_product = 0
        # Try all disjoint palindrome pairs
        for i in range(len(palindromes)):
            for j in range(i + 1, len(palindromes)):
                m1, l1 = palindromes[i]
                m2, l2 = palindromes[j]
                if m1 & m2 == 0:  # disjoint
                    max_product = max(max_product, l1 * l2)

        return max_product