class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        mydict = {}
        for _, num in enumerate(nums):
            if num in mydict:
                return True
            mydict[num] = True
        return False