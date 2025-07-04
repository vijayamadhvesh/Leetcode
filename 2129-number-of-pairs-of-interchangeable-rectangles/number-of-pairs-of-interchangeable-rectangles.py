class Solution:
    def interchangeableRectangles(self, rectangles: List[List[int]]) -> int:
        res = 0
        d = Counter()
        for w, h in rectangles:           
            res += d[w/h]
            d[w/h] += 1
            
        return res