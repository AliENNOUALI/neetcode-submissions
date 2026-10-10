class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t) : return False
        ht ={}
        hs ={}
        for i in range(len(s)):
            hs[s[i]]= 1+ hs.get(s[i] ,0 )
            ht[t[i]]= 1+ ht.get(t[i] ,0 )

        for j in range(len(s)):
            if t[j] not in hs.keys():
                return False
            if ht[t[j]] != hs[t[j]]:
                return False

           
        return True 
