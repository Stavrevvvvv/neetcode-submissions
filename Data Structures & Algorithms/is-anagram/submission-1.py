class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        ssorted = ''.join(sorted(s))
        tsorted = ''.join(sorted(t))

        if ssorted == tsorted:
            return True
        else:
            return False