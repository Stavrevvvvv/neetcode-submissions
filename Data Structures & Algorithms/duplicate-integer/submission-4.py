class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        hasdup = set()

        for n in nums:
            if n not in hasdup:
                hasdup.add(n)
            else: 
                return True
        return False
