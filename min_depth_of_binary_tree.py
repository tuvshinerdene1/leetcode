# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
from typing import Optional


class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        # if the left child is missing, we must look down the right branch
        if not root.left:
            return 1 + self.minDepth(root.right)

        # if the right child is missing, we must look down the left branch
        if not root.right:
            return 1 + self.minDepth(root.left)

        # if the both children exist, take the minimum of both paths
        return 1 + min(self.minDepth(root.left), self.minDepth(root.right))