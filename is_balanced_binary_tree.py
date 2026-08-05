# 110. Balanced Binary Tree

# Given a binary tree, determine if it is .

 
# Example 1:
# Input: root = [3,9,20,null,null,15,7]
# Output: true

# Example 2:
# Input: root = [1,2,2,3,3,null,null,4,4]
# Output: false

# Example 3:
# Input: root = []
# Output: true


# Constraints:

#     The number of nodes in the tree is in the range [0, 5000].
#     -104 <= Node.val <= 104

from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        # helper function returns the height of the tree if balanced,
        # or -1 if the tree is unbalanced
        def get_height(node:Optional[TreeNode]) -> int:
            # base case: an empty tree has height of 0 and is balanced
            if not node:
                return 0
            # step 1: recursively get the height of the left subtree
            left_height = get_height(node.left)

            # step 2: short-circuit if the left subtree is already unbalanced
            if left_height == -1:
                return -1

            # step 3: recursively get the height of the right subtree
            right_height = get_height(node.right)

            # step 4: short-circuit if the right subtree is already unbalanced
            if right_height == -1:
                return -1

            # step 5: check if the current node violates the balance condition
            if abs(left_height - right_height) > 1:
                return -1 # mark this subtree as unbalanced

            # step 6: if everything is balanced, return the actual height of the current node
            return max(left_height, right_height) + 1

        return get_height(root) != 1
    
