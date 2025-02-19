# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        v1=""
        v2=""

        while not l1==None:
            v1=str(l1.val)+v1
            l1=l1.next
        while not l2==None:
            v2=str(l2.val)+v2
            l2=l2.next
            
        vr=str(int(v1)+int(v2))
        r=ListNode()
        now=r
        for i in range(1,len(vr)+1):
            now.val=vr[-i]
            if i<len(vr):
                now.next=ListNode()
                now=now.next
        return r
