class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        arr=sorted(list(set(nums)))
        count=len(arr)

        for i in range(count):
            nums[i]=arr[i]
        return count
