# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        while root:
            if p.val < root.val and q.val < root.val:
                root = root.left                        #if both p&q are smaller than root,set root to its left child
            elif p.val > root.val and q.val > root.val:
                root = root.right                       #if both p&q are greater than root,set root to its right child
            else:
                return root
        