class Solution:
    def reverseBits(self, n: int) -> int:
        r=""
        b=bin(n)

        for i in range(1,32+1):
            if i>len(b)-2:
                r+="0"
            else:
                r+=b[-i]
        return int(r,2)
