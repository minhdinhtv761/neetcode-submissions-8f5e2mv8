class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        freq = defaultdict(int)
        for c in s:
            freq[c] += 1
        for c in t:
            freq[c] -=1
        return all(v == 0 for v in freq.values())