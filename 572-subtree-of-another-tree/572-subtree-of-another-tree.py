# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not subRoot:                                             #if not sub return True
            return True
        if not root:
            return False
        if self.sameTree(root,subRoot):                             #check the base trees
            return True
        else:                                                       #else change root to left or right
            return (self.isSubtree(root.left,subRoot) or self.isSubtree(root.right,subRoot))
            
    def sameTree(self,p,q):                                         #same tree to check the root and subroot
        if not p and not q:
            return True
        if p and q and p.val == q.val:                              #if both values same,check their children
            return (self.sameTree(p.right,q.right) and self.sameTree(p.left,q.left))
        return False                                                #if values not same return false
            
        