class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        orderS = sorted(s)
        orderT = sorted(t)

        if orderS == orderT:
            return True
        else:
            return False