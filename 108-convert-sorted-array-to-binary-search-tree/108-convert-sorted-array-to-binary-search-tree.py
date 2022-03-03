# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        if not nums:
            return None
        mid = len(nums)//2                              #find mid index
        root = TreeNode(nums[mid])
        root.left = self.sortedArrayToBST(nums[:mid])   #construct left tree passing till mid
        root.right = self.sortedArrayToBST(nums[mid+1:])#simillarly for right tree
        
        return root                                     #return root