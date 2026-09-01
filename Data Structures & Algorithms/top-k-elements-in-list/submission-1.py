class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counter = defaultdict(int)

        for num in nums:
            counter[num] += 1

        topk = sorted(counter, key=counter.get, reverse=True)[:k]

        return topk