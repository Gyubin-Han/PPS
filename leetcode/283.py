class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        s=0
        z=0
        for i in range(len(nums)):
            v=nums[i]

            if v==0:
                z+=1
            else:
                nums[s]=v
                s+=1
        for i in range(1,z+1):
            nums[-i]=0
