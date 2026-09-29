func isAnagram(s string, t string) bool {
    count := make(map[rune]int)
    for _, c := range s {
        count[c]++
    }
    for _, c := range t {
        count[c]--
    }
    for k := range count {
        if count[k] != 0 {
            return false
        }
    }
    return true
}
