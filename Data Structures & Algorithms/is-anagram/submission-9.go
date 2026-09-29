func isAnagram(s string, t string) bool {
    if len(s) != len(t) {
        return false
    }
    countS, countT := make(map[rune]int), make(map[rune]int)
    for i, c := range s {
        countS[c]++
        countT[rune(t[i])]++
    }
    for i, v := range countS {
        if countT[i] != v {
            return false
        }
    }
    return true
}
