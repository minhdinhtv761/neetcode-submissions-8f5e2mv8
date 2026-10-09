class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        zero_loc = -1
        final_product = 1
        res = [0] * len(nums)
        for idx, num in enumerate(nums):
            if num == 0:
                if zero_loc != -1:
                    return res
                zero_loc = idx
                continue
            final_product *= num
        if zero_loc != -1:
            res[zero_loc] = final_product
            return res
        for idx, num in enumerate(nums):
            res[idx] = final_product//num
        return res