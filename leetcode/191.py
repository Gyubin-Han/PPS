class Solution:
    def hammingWeight(self, n: int) -> int:
        count=0
        b=bin(n)

        for i in range(2,len(b)):
            if b[i]=="1":
                count+=1
        return count
