# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        l=[]
        while not head==None:
            n=ListNode(head.val)
            l.append(n)
            head=head.next
        
        r=ListNode()
        rt=r
        while len(l)>0:
            rt.next=l.pop()
            rt=rt.next
        return r.next
