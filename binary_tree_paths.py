# 257. Binary Tree Paths

# You are given the root of a binary tree.

# Return all root-to-leaf paths in any order.

# A leaf is a node with no children.

 

# Example 1:

# Input: root = [1,2,3,null,5]
# Output: ["1->2->5","1->3"]

# Example 2:

# Input: root = [1]
# Output: ["1"]


class TreeNode:
    def __init__(self, val=0, left= None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def binaryTreePaths(self, root:TreeNode | None) -> list[str]:
        if not root:
            return []

        stack = [(root, str(root.val))]
        paths = []

        while stack:
            node, path = stack.pop()

            if not node.left and not node.right:
                paths.append(path)

            if node.right:
                stack.append((node.right, path + "->" + str(node.right.val)))

            if node.left:
                stack.append((node.left, path + "->" + str(node.left.val)))
        return paths

    def binaryTreePaths(self, root:TreeNode | None) -> list[str]:
        if not root:
            return []

        paths = []

        def dfs(node:TreeNode, current_path:str):
            if not node.left and not node.right:
                paths.append(current_path)
                return

            if node.left:
                dfs(node.left, current_path + "->" + str(node.left.val))

            if node.right:
                dfs(node.right, current_path + "->" + str(node.right.val))

        dfs(root, str(root.val))
        return paths
        
