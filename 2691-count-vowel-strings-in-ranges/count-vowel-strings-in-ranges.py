class Solution:
    def vowelStrings(self, words: List[str], queries: List[List[int]]) -> List[int]:
        res = []
        vowels = {'a', 'e', 'i', 'o', 'u'}
        vowels_count = [0]*(len(words)+1)
        for i, word in enumerate(words):
            if word[0] in vowels and word[-1] in vowels:
                vowels_count[i+1] = vowels_count[i]+1
            else:
                vowels_count[i+1] = vowels_count[i]
        print(vowels_count)

        for start, end in queries:
            res.append(vowels_count[end+1] - vowels_count[start])
            
        return res