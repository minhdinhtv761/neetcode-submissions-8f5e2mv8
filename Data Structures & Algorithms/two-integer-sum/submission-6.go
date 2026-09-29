func twoSum(nums []int, target int) []int {
    m := make(map[int]int)
	for big, v := range nums {
		small, ok := m[target-v]
		if ok {
			return []int{small, big}
		}
		m[v] = big
	}
	return []int{}
}
