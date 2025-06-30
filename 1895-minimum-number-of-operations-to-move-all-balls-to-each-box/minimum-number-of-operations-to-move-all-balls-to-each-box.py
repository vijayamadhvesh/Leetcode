class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        
        res = []
        n = len(boxes)

        

        for i in range(n):
            balls_count = 0
            for j in range(n):
                if boxes[j] == '1':
                    balls_count += abs(i-j) 
            res.append(balls_count)
        return res