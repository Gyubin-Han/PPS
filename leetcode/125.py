import re
class Solution:
    def isPalindrome(self, s: str) -> bool:
        ns=re.sub(r"[^A-Za-z0-9]","",s).lower()
        
        isPal=True
        for i in range(len(ns)//2):
            if not ns[i]==ns[-i-1]:
                isPal=False
                break
        return isPal
