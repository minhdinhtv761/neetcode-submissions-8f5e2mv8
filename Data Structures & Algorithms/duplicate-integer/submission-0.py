class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        exist_map = {}
        for num in nums:
            if num in exist_map:
                return True
            exist_map[num] = True
        return False