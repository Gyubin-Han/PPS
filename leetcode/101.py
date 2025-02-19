# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def leftSearch(self,stack:List[TreeNode],now:Optional[TreeNode]):
        if now==None:
            stack.append(None)
        else:
            stack.append(now.val)
            self.leftSearch(stack,now.left)
            self.leftSearch(stack,now.right)
    def rightSearch(self,stack:List[TreeNode],now:Optional[TreeNode]) -> bool:
        if len(stack)<1:
            return False
        if now==None:
            if not(stack.pop()==now):
                return False
            return True
        elif not self.rightSearch(stack,now.left):
            return False
        elif not self.rightSearch(stack,now.right):
            return False
        elif not stack.pop()==now.val:
            return False
        return True

    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        stack=[]
        self.leftSearch(stack,root.left)
        isSym=self.rightSearch(stack,root.right)

        if isSym and len(stack)==0:
            return True
        else:
            return False
