# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        l=[]
        while not head==None:
            l.append(head.val)
            head=head.next
        
        for i in range(len(l)//2):
            if not l[i]==l[-i-1]:
                return False
        return True
