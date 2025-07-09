class Solution:
    def maxFreeTime(self, eventTime: int, k: int, startTime: List[int], endTime: List[int]) -> int:
        n = len(startTime)
        gaps = []

        # Initial gap before first meeting
        gaps.append(startTime[0] - 0)

        # Gaps between meetings
        for i in range(1, n):
            gaps.append(startTime[i] - endTime[i-1])

        # Gap after last meeting
        gaps.append(eventTime - endTime[-1])

        # Sliding window of size k + 1
        max_free = 0
        window_sum = sum(gaps[:k+1])
        max_free = window_sum

        for i in range(k+1, len(gaps)):
            window_sum += gaps[i] - gaps[i - (k+1)]
            max_free = max(max_free, window_sum)

        return max_free