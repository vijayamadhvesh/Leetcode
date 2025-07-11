class Solution:
    def mostBooked(self, n: int, meetings: List[List[int]]) -> int:
        meetings.sort()
        count = [0] * n
        free = list(range(n))
        heapq.heapify(free)
        busy = []  # (endTime, room)

        for start, end in meetings:
            while busy and busy[0][0] <= start:
                _, room = heapq.heappop(busy)
                heapq.heappush(free, room)

            if free:
                room = heapq.heappop(free)
                heapq.heappush(busy, (end, room))
                count[room] += 1
            else:
                earliest_end, room = heapq.heappop(busy)
                heapq.heappush(busy, (earliest_end + (end - start), room))
                count[room] += 1

        max_count = max(count)
        return count.index(max_count)