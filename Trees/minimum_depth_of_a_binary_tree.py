from typing import Optional
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        """Solved with BFS"""

        q = []
        if not root:
            return 0
        
        q.insert(0, (root, 1))
        while q:
            v, curr_depth = q.pop()

            if not v.left and not v.right:
                return curr_depth

            if v.left:
                q.insert(0, (v.left, curr_depth + 1))
            if v.right:
                q.insert(0, (v.right, curr_depth + 1))


l = TreeNode(val=15)
r = TreeNode(val=7)
left = TreeNode(val=9)
right = TreeNode(val=20, left=l, right=r)
root = TreeNode(val=3, left=left, right=right)

s = Solution()
s.minDepth(root)