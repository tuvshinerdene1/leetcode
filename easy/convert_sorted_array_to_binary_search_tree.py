# Given an integer array nums where the elements are sorted in ascending order, convert it to a binary search tree.

 

# Example 1:

# Input: nums = [-10,-3,0,5,9]
# Output: [0,-3,9,-10,null,5]
# Explanation: [0,-10,5,null,-3,null,9] is also accepted:

# Example 2:

# Input: nums = [1,3]
# Output: [3,1]
# Explanation: [1,null,3] and [3,1] are both height-balanced BSTs.

# Definition for a binary tree node.
from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        def helper(left:int, right:int) -> Optional[TreeNode]:
            if left > right:
                return None

            mid = (left + right) // 2

            root = TreeNode(nums[mid])

            root.left = helper(left, mid  - 1)
            root.right = helper(mid + 1, right)

            return root
        return helper(0, len(nums) - 1)


class Solution_iterative:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        if not nums:
            return None

        # create the root node
        total_mid = len(nums) // 2
        root = TreeNode(nums[total_mid])

        # Stack stores tuples : (current_node, left_index, right_index)
        stack = [(root, 0, len(nums) - 1)]

        while stack:
            node, left, right = stack.pop()
            mid = (left + right) // 2

            if left <= mid - 1:
                left_mid = (left + mid - 1) // 2
                node.left = TreeNode(nums[left_mid])
                stack.append((node.left, left, mid-1))

            if mid + 1 <= right:
                right_mid = (mid + 1 + right) // 2
                node.right = TreeNode(nums[right_mid])
                stack.append((node.right, mid + 1, right))

        return root
        