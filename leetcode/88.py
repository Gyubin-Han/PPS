class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        narr=[]
        cnt1=0
        cnt2=0

        while cnt1<m and cnt2<n:
            v=0
            if nums1[cnt1]<nums2[cnt2]:
                v=nums1[cnt1]
                cnt1+=1
            else:
                v=nums2[cnt2]
                cnt2+=1
            narr.append(v)
        while cnt1<m:
            narr.append(nums1[cnt1])
            cnt1+=1
        while cnt2<n:
            narr.append(nums2[cnt2])
            cnt2+=1

        for i in range(n+m):
            nums1[i]=narr[i]
