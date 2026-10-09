func productExceptSelf(nums []int) []int {
    n := len(nums)
    prefixes := make([]int, n, n)
    suffixes := make([]int, n, n)
    res := make([]int, n, n)
    prefixes[0], suffixes[n-1] = 1, 1
    
    for i := 1; i < n; i++ {
        prefixes[i] = prefixes[i-1] * nums[i-1]
    }

    for i := n-2; i >= 0; i-- {
        suffixes[i] = suffixes[i+1] * nums[i+1]
    }

    for i, v := range prefixes {
        res[i] = v * suffixes[i]
    }

    return res
}
