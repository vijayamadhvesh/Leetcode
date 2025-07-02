class Solution:
    def frequencySort(self, s: str) -> str:
         # Allocate frequency array for ASCII range from 'A'(65) to 'z'(122)
        char_freq = [0] * (ord('z') - ord('0') + 1)  # size = 58

        for char in s:
            char_freq[ord(char) - ord('0')] += 1

        # Build (char, frequency) pairs
        freq_pairs = []
        for i, freq in enumerate(char_freq):
            if freq > 0:
                char = chr(ord('0') + i)
                freq_pairs.append((freq, char))

        # Sort by decreasing frequency
        freq_pairs.sort(reverse=True)
        # Build result string
        res = ''
        for freq, char in freq_pairs:
            res += char * freq

        return res