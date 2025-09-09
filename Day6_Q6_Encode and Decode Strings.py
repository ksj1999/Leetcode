
class Solution:

    def encode(self, strs: List[str]) -> str:
        
        dic = {}
        s = strs[0]

        for i in strs:
            dic[i] = len(i)
        print(dic)

        for i in range(1, len(strs)):
            s += strs[i]
            print(s)
        return s

  ---------------------------------


class Solution:

    def encode(self, strs: List[str]) -> str:
        dic = {}
        for word in strs:
            l = len(word)
            if l not in dic:
                dic[l] = []
            dic[l].append(word)

        print("len dic:", dic)

        return "".join(strs), dic

    def decode(self, s: str, dic: dict) -> List[str]:
        res = []
        i = 0
        for length, words in dic.items():
            for _ in words:
                res.append(s[i:i+length])
                i += length
        return res
---------------------------------------------------

class Solution:
    def encode(self, strs: List[str]) -> str:
        out = []
        for w in strs:
            out.append(str(len(w)) + "#" + w)
        return ''.join(out)

    def decode(self, s: str) -> List[str]:
        res, i, n = [], 0, len(s)
        while i < n:
            j = i
            while s[j] != "#":
                j += 1
            L = int(s[i:j])
            res.append(s[j+1:j+1+L])
            i = j + 1 + L
        return res

