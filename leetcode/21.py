# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        result=ListNode()
        re=result
        li1=list1
        li2=list2

        while not li1==None and not li2==None:
            n=ListNode()
            if li1.val<li2.val:
                n.val=li1.val
                li1=li1.next
            else:
                n.val=li2.val
                li2=li2.next
            re.next=n
            re=re.next
        
        while not li1==None:
            n=ListNode()
            n.val=li1.val
            re.next=n
            re=re.next
            li1=li1.next
        while not li2==None:
            n=ListNode()
            n.val=li2.val
            re.next=n
            re=re.next
            li2=li2.next
        
        return result.next
