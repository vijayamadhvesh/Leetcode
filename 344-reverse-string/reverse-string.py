class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        res = ''
        j = len(s)-1
        for i in range(len(s)//2):
            s[i], s[j] = s[j], s[i]
            j-=1
            