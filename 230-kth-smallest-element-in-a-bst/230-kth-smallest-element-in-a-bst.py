# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        n=0
        stack=[[root]]
        
        while stack:                    #if root, append to stack
            while root:
                stack.append(root)      
                root=root.left          #basic inorder traversal
            root=stack.pop()
            n+=1                        #increment counter and compare to k
            
            if n == k:                  #if equal, found the kth element
                return root.val
            root=root.right            