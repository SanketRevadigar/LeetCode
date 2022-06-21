# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, node: Optional[TreeNode]) -> Optional[TreeNode]:
        if not node:
            return None                                             #base case if no node return None
        
        temp = node.right                                           #swap the children
        node.right = node.left
        node.left = temp
        
        self.invertTree(node.left)                                  #call recursion for both children
        self.invertTree(node.right)
        
        return node
        
        #time complexity is O(n), where nnn is the number of nodes in the tree
        #space complexity is O(n)