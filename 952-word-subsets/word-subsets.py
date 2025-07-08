class Solution:
    def wordSubsets(self, words1: List[str], words2: List[str]) -> List[str]:
        max_count = Counter()
        for b in words2:
            b_count = Counter(b)
            for char in b_count:
                max_count[char] = max(max_count[char], b_count[char])

        
        result = []
        for word in words1:
            word_count = Counter(word)
        
            if all(word_count[char] >= max_count[char] for char in max_count):
                result.append(word)

        return result