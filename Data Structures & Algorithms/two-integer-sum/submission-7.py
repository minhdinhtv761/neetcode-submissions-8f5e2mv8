class Solution:
	def twoSum(self, nums: List[int], target: int) -> List[int]:
		m = {}
		for big, val in enumerate(nums):
			if target-val in m:
				return [m[target-val], big]
			m[val] = big
		return []