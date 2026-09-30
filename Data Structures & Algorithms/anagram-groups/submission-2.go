func groupAnagrams(strs []string) [][]string {
    res := make(map[[26]int][]string)
    for _, str := range strs {
        var count [26]int
        for _, c := range str {
            count[c-'a']++
        }
        res[count] = append(res[count], str)
    }

    finalRes := make([][]string, len(res))
    idx := 0
    for _, group := range res {
        finalRes[idx] = group
        idx++
    }

    return finalRes
}
