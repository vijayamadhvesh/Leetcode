class Solution:
    def interchangeableRectangles(self, rectangles: List[List[int]]) -> int:
        res = 0
        freq = Counter()
        for w,h in rectangles:
            freq[w/h]+=1

        for val in freq.values():
            if val > 1:
                cal = val*(val -1) //2
                res += cal
        return res