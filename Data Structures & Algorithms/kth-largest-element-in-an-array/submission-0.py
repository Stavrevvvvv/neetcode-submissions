class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:

        maxHeap = []
        for n in nums:
            maxHeap.append(-n)
        
        heapq.heapify(maxHeap)
        res = 0
        for i in range(1, k):
            heapq.heappop(maxHeap)
        return -maxHeap[0]
            

