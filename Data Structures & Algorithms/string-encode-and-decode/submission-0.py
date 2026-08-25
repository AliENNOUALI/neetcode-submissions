class Solution:

    def encode(self, strs: List[str]) -> str:
        a = ""
        for st in strs:
            a += str(len(st)) + "#" + st
        return a

            
        
    def decode(self, s: str) -> List[str]:
        ls = []
        i = 0
        while i < len(s):   
            j = i
            while s[j] != "#":
                j += 1
            length = int(s[i:j])
            ls.append(s[j+1 : 1+j+length])
            i = j + length + 1
        return ls


