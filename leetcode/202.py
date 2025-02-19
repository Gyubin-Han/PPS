class Solution:
    def isHappy(self, n: int) -> bool:
        s=str(n)
        while not len(s)==1:
            r=0
            for i in range(len(s)):
                r+=int(s[i])**2
            s=str(r)
        
        if s=="1" or s=="7":
            return True
        else:
            return False
