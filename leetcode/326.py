class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        last=1
        while last<n:
            last*=3
        if last==n:
            return True
        else:
            return False
