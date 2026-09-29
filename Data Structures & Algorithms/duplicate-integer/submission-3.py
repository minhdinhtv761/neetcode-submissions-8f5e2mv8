class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        m = defaultdict(bool)
        for v in nums:
            if not m[v]:
                m[v] = True
                continue
            else:
                return True
        return False