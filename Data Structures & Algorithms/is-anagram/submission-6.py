class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        ms = defaultdict(int)
        mt = defaultdict(int)
        for v in s:
            ms[v] += 1
        for v in t:
            mt[v] += 1
        return ms == mt