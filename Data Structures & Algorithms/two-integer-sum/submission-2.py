class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hash_map = {}
        for i, cur in enumerate(nums):
            diff = target - cur
            if diff in hash_map:
                return [hash_map[diff], i]
            hash_map[cur] = i
        return []