class Solution:
    def isValid(self, s: str) -> bool:
        par = {")":"(", "]": "[", "}": "{" }
        if len(s) % 2 : return False
        ls = [0]
        if s[0] in ")]}" : return False
        for i in range(len(s)):
            if s[i] in ["(","[","{"]:
                ls.append(s[i])
            else:
                if ls[-1] == par[s[i]]:
                    ls.pop()
                else:
                    return False
                if not ls : return 
        if ls == [0]:
            return True            
        return False
            
        