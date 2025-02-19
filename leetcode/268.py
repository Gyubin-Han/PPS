class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        last=-1
        nums.sort()
        for i in range(len(nums)):
            if not last+1==nums[i]:
                break
            else:
                last+=1
        
        return last+1
