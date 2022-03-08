# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if root == p or root == q:              # If looking for me, return myself
            return root
        
        left = right =None                      # else look in left and right child
        
        if root.left:
            left=self.lowestCommonAncestor(root.left,p,q)
        
        if root.right:
            right=self.lowestCommonAncestor(root.right,p,q)
        
        if left and right:                      # if both children returned a node, means
            return root                         # both p and q found so parent is LCA
        else:
        # either one of the chidren returned a node, meaning either p or q found on left or right branch.
        # Example: assuming 'p' found in left child, right child returned 'None'. This means 'q' is
        # somewhere below node where 'p' was found we dont need to search all the way, 
        # because in such scenarios, node where 'p' found is LCA
            return left or right
        