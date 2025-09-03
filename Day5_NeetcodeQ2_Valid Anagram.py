class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        slist = []
        tlsit = []
        for i in s:
            slist.append(i)
        for i in t:
            tlsit.append(i)
        
        print(slist,tlsit)

        sorts = sorted(slist)
        sortt = sorted(tlsit)

        if sorts == sortt:
            print(sorts,sortt)
            return True

        return False


-------------------------------


