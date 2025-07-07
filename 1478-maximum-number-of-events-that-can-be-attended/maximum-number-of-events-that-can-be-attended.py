class Solution:
    def maxEvents(self, events: List[List[int]]) -> int:
        events.sort()
        min_day = min(event[0] for event in events)
        max_day = max(event[1] for event in events)
        
        i = 0
        res = 0
        n = len(events)
        heap = []

        for day in range(min_day, max_day + 1):
            # Add events starting today
            while i < n and events[i][0] == day:
                heapq.heappush(heap, events[i][1])
                i += 1
            
            # Remove past events
            while heap and heap[0] < day:
                heapq.heappop(heap)
            
            # Attend the event that ends the earliest
            if heap:
                heapq.heappop(heap)
                res += 1
        
        return res

        