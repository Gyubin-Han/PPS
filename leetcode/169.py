class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        nums.sort()
        print(nums)
        last=(nums[0],1)
        mx=last

        for i in range(1,len(nums)):
            if nums[i]==last[0]:
                last=(last[0],last[1]+1)
            else:
                last=(nums[i],1)

            if mx[1]<last[1]:
                mx=last
        return mx[0]
