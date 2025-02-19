# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        al=set()

        r=None
        a=headA
        b=headB
        while a:
            al.add(a)
            a=a.next
        while b:
            if b in al:
                r=b
                break
            b=b.next
        
        return r
