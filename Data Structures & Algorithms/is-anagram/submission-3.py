class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        hashMap = {}

        s = sorted(s)
        t = sorted(t)

        if s == t: return True
        else: return False