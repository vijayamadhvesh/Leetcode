class Solution:
    def interchangeableRectangles(self, rectangles: List[List[int]]) -> int:
        res = 0
        temp =[]
        for w,h in rectangles:
            temp.append(w/h)

        freq = Counter(temp)
        for val in freq.values():
            if val > 1:
                cal = val*(val -1) //2
                res += cal
        return res