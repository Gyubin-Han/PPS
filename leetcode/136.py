class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        nums.sort()
        last=nums[0]
        count=1

        for i in range(1,len(nums)):
            if not last==nums[i]:
                if count==1:
                    break
                last=nums[i]
                count=1
            else:
                count+=1
        return last
