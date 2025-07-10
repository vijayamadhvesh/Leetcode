class Solution:
    def maxFreeTime(self, eventTime: int, startTime: List[int], endTime: List[int]) -> int:
        n = len(endTime)
        preLarge = [0]*(n+1)
        postLarge = [0]*(n+1)

        intervals = []
        s = 0
        for i in range(n):
            intervals.append(startTime[i]-s)
            s = endTime[i]
            preLarge[i+1] = max(preLarge[i], intervals[i])
        intervals.append(eventTime - s)
        for i in range(n):
            postLarge[n-i-1] = max(postLarge[n-i], intervals[n-i])
        maxL = 0
        # print(preLarge)
        # print(postLarge)
        # print(intervals)

        for i in range(n):
            curr = endTime[i] - startTime[i]
            if preLarge[i] >= curr or postLarge[i+1] >= curr:
                maxL = max(maxL, curr + intervals[i] + intervals[i+1])
            else:
                maxL = max(maxL, intervals[i] + intervals[i+1])

        return maxL