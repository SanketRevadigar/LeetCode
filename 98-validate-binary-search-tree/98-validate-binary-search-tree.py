# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def validate(node,low,high):                        #create a helper function to check validity
            if not node:
                return True                                 #empty tree is a binary tree
            if not(node.val>low and node.val<high):         #if the condition doesnt hold true return False
                return False
            return (validate(node.left,low,node.val) and validate(node.right,node.val,high))    #check for left and right child
       
        return (validate(root,float('-inf'),float('inf')))  #set low and high to extreme large values
        
        