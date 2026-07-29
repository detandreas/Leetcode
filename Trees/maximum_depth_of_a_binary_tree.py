from typing import Optional
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __str__(self):
        return f"{self.val}"

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        """DFS approach"""
        # a stack containing tuples (vertex, depth)
        stack = []
        
        if not root:
            return 0
        
        stack.append((root, 1))
        depth = 0
        while stack:
            v, curr_depth = stack.pop()
            depth = max(depth, curr_depth)

            if v.left:
                stack.append((v.left, curr_depth + 1))
            if v.right:
                stack.append((v.right, curr_depth + 1))

        return depth

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))
        


l = TreeNode(val=15)
r = TreeNode(val=7)
left = TreeNode(val=9)
right = TreeNode(val=20, left=l, right=r)
root = TreeNode(val=3, left=left, right=right)

s = Solution()
s.maxDepth(root)