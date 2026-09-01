class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        minHeap: list[tuple[int, list[int]]] = []

        for point in points:
            heapq.heappush(minHeap, (point[0]**2 + point[1]**2, point))
        res = []
        for _ in range(k):
            _, pt = heapq.heappop(minHeap)
            res.append(pt)
        return res