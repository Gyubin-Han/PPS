class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        l=set()
        isDu=False
        for i in nums:
            if i in l:
                isDu=True
                break
            else:
                l.add(i)
        return isDu
