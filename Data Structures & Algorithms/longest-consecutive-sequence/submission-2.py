class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums_set = set(nums)
        res = 0
        for num in nums_set:
            length = 1
            if num-1 in nums_set:
                continue
            while num+length in nums_set:
                length += 1
            if res < length:
                res = length
        return res