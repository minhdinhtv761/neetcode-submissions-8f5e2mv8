type Solution struct{}

func (s *Solution) Encode(strs []string) string {
    if len(strs) == 0 {
        return ""
    }
    lens := make([]string, len(strs), len(strs))
    for i, str := range strs {
        lens[i] = strconv.FormatInt(int64(len(str)), 10)
    }
    return strings.Join(lens, ",") + "#" + strings.Join(strs, "")
}

func (s *Solution) Decode(encoded string) []string {
    if encoded == "" {
        return []string{}
    }
    parts := strings.SplitN(encoded, "#", 2)
    lens := strings.Split(parts[0], ",")
    strs := make([]string, len(lens), len(lens))
    cur := 0
    for i, l := range lens {
        v, _ := strconv.Atoi(l)
        strs[i] = parts[1][cur:cur+v]
        cur = cur+v
    }
    return strs
}
