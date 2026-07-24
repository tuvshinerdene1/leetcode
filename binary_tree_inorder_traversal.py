# Given the root of a binary tree, return the inorder traversal of its nodes' values.
 
# Example 1:
# Input: root = [1,null,2,3]
# Output: [1,3,2]


# Example 2:
# Input: root = [1,2,3,4,5,null,8,null,null,6,7,9]
# Output: [4,2,6,5,7,1,3,9,8]


# Example 3:
# Input: root = []
# Output: []

# Example 4:
# Input: root = [1]
# Output: [1]

from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def inorderTraversal(self, root:Optional[TreeNode]) -> List[int]:
        result = []
        def traverse(node):
            if not node:
                return
            traverse(node.left)
            result.append(node.val)
            traverse(node.right)
        traverse(root)
        return result


class Solution_iterative:
    def inorderTraversal(self, root:Optional[TreeNode]) -> List[int]:
        result = []
        stack = []
        curr = root

        while curr or stack:
            while curr:
                stack.append(curr.val)
                curr = curr.left

            curr = stack.pop()
            result.append(curr.val)

            curr = curr.right

        return result 