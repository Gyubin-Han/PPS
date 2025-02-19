class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        dnum={}
        for i in range(26):
            dnum[chr(ord('A')+i)]=i+1

        result=0
        for i in range(1,len(columnTitle)+1):
            c=columnTitle[-i]
            result+=dnum[c]*(26**(i-1))
        return result
