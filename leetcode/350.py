class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        result=[]
        check={}

        for i in nums1:
            if i in check:
                check[i]+=1
            else:
                check[i]=1
        for i in nums2:
            if i in check and check[i]>0:
                check[i]-=1
                result.append(i)
        return result
