class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        heapStones = []

        for stone in stones:
            heapStones.append(-stone)
        
        heapq.heapify(heapStones)        

        while len(heapStones) > 1:
            strongest1 = -heapq.heappop(heapStones)
            strongest2 = -heapq.heappop(heapStones)
            if strongest1 != strongest2:
                heapq.heappush(heapStones, -(strongest1 - strongest2))
        if heapStones:
            return -heapStones[0]
        return 0

