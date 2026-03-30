class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        hash_map = {}
        for c in s:
            if c not in hash_map:
                hash_map[c] = 0
            hash_map[c] += 1
        for c in t:
            if c not in hash_map:
                return False
            hash_map[c] -= 1
            if hash_map[c] == 0:
                del hash_map[c]
        return len(hash_map) == 0