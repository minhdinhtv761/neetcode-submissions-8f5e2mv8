class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums_set = set(nums)
        res = 0
        for num in nums:
            nums_set.add(num)
        for num in nums_set.copy():
            if num not in nums_set:
                continue
            tmp = 1
            prev = num - 1
            while prev in nums_set:
                tmp += 1
                nums_set.remove(prev)
                prev -= 1
            nex = num + 1
            while nex in nums_set:
                tmp += 1
                nums_set.remove(nex)
                nex += 1
            if res < tmp:
                res = tmp
        return res