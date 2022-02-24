# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if not preorder or not inorder:                                 #if 2 lists are not given, return False
            return None
        root=TreeNode(preorder[0])                                      #set root first element of preorder
        mid=inorder.index(preorder[0])                                  #mid will be the index of root in inorder
        root.left=self.buildTree(preorder[1:mid+1],inorder[:mid])       #build left tree
        root.right=self.buildTree(preorder[mid+1:],inorder[mid+1:])     #build right tree
        return root
        
        #Time Complexity - O(N)
        #Space Complexity - O(N)