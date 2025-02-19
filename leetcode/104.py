# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def depth(self,now:Optional[TreeNode],depth:int):
        if now==None:
            return depth-1
        return max(self.depth(now.left,depth+1),self.depth(now.right,depth+1),depth)
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        return self.depth(root,1)
