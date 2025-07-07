class Solution:
    def findMatrix(self, nums: List[int]) -> List[List[int]]:
        res = []
        counter = Counter(nums)

        while counter:
            temp = []
            # Use list(counter) to avoid modifying during iteration
            for key in list(counter):
                temp.append(key)
                counter[key] -= 1
                if counter[key] == 0:
                    del counter[key]
            res.append(temp)

        return res