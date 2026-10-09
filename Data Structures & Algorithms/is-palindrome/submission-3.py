class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.replace(" ", "")
        clean = "".join(c.lower() for c in s if c.isalnum())
        n = len(clean)
        a=0
        for i in range(n//2 + n%2):
            if clean[i] != clean[n-i-1]:
                return False
                break
        return True

        
         
                
            

            
        