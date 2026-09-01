class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashMap = {}

        for word in strs:
            sorted_word = ''.join(sorted(word))
            
            if sorted_word not in hashMap:
                hashMap[sorted_word] = []
            hashMap[sorted_word].append(word)

        return list(hashMap.values())