class Solution:
    def frequencySort(self, s: str) -> str:
        freq_map = Counter(s)
        sorted_chars = sorted(freq_map.items(), key=lambda x: -x[1])
        print(sorted_chars)
        res = ''
        for char, freq in sorted_chars:
            res += char * freq
        return res