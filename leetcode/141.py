# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        h2=head
        while h2 and h2.next:
            head=head.next
            h2=h2.next.next
            if head==h2:
                return True
        return False
