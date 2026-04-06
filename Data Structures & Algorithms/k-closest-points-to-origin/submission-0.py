import heapq

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap = []
        for x, y in points:
            d = x**2 + y**2
            heapq.heappush(heap, (d, [x, y]))

        return [heapq.heappop(heap)[1] for _ in range(k)]
