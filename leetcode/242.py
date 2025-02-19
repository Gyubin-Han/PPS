class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        d={}

        if not len(s)==len(t):
            return False
        for i in s:
            if i in d:
                d[i]+=1
            else:
                d[i]=1
        for i in t:
            if i in d:
                d[i]-=1
            else:
                return False
        
        for i in d.keys():
            if not d[i]==0:
                return False
        return True
