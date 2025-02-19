# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorder(self, now: Optional[TreeNode], result: List[int]):
        if not now.left==None:
            self.inorder(now.left,result)
        result.append(now.val)
        if not now.right==None:
            self.inorder(now.right,result)

    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        result=[]
        if not root==None:
            self.inorder(root,result)
        
        return result
