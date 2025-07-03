class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        def merge(s, m, e):
            L, R = nums[s:m+1], nums[m+1:e+1]

            i,j,k = 0,0,s

            while i<len(L) and j<len(R):
                if L[i]<R[j]:
                    nums[k] = L[i]
                    i += 1
                else:
                    nums[k] = R[j]
                    j += 1
                k += 1
            
            while i<len(L):
                nums[k] = L[i]
                i, k =  i+1, k+1

            while j<len(R):
                nums[k] = R[j]
                j,k = j+1, k+1

        
        def mergeSort(s, e):
            if e==s:
                return nums
            
            m = (s+e)//2

            mergeSort(s, m)
            mergeSort(m+1, e)

            merge(s, m, e)
            
            return nums


        return mergeSort(0, len(nums)-1)