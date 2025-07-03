class Solution:
    def checkPossibility(self, nums: List[int]) -> bool:
        count = 0
        for i in range(len(nums)-1):
            if nums[i+1] < nums[i]:
                count += 1
                if count > 1:
                    return False

                if i == 0 or nums[i - 1] <= nums[i + 1]:
                    nums[i] = nums[i + 1]  # lower current
                else:
                    nums[i + 1] = nums[i]  # raise next
        
        return True