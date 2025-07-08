class Solution:
    def sortJumbled(self, mapping: List[int], nums: List[int]) -> List[int]:
        def convert(num):

            result = [str(mapping[int(i)]) for i in str(num)]
            
            return int(''.join(result))
        nums.sort(key = convert)
        return nums