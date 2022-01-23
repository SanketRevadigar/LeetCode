# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        q = deque()
        q.append(root)
        res = []
        while q:
            level = []                              #variable for each level
            for i in range(len(q)):                 #typical bfs iterating loops
                node = q.popleft()
                if node:
                    level.append(node.val)          #append each values to level by level
                    q.append(node.left)
                    q.append(node.right)
            if level:                               #edge case for not add empty level
                res.append(level)
        return res
    