class Solution:
    def longestCommonPrefix(self, arr1: List[int], arr2: List[int]) -> int:
        # all comb of arr1
        comb_arr1 = set()
        for num in arr1 :
            while num > 0 and num not in comb_arr1:
                comb_arr1.add(num)
                num //= 10
        print(comb_arr1)
        # all comb of arr2
        ans = -1
        for num in arr2 :
            while num > 0 :
                if num in comb_arr1 :
                    ans = max(ans, num)
                    break
                num //= 10
        if ans == -1 : return 0
        else : return len(str(ans))