class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""
        for s in strs:
            res = res + str(len(s)) + "," + s
        return res

    def decode(self, s: str) -> List[str]:
        res = []
        i, j = 0, 1
        while i < len(s):
            if s[j] != ",":
                j += 1
                continue
            cur_len = int(s[i:j])
            i = j+1
            cur = s[i:i+cur_len]
            res.append(cur)
            i = i+cur_len
            j = i+1
        return res




