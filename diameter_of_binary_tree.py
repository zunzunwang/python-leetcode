from typing import List


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        if root is None:
            return 0
        global_max = [0]
        self.get_depth_max(root, global_max)
        return global_max[0]

    def get_depth_max(self, root: TreeNode, global_max: List[int]):
        if root is None:
            return 0

        left_depth = self.get_depth_max(root.left, global_max)
        right_depth = self.get_depth_max(root.right, global_max)
        local_max = left_depth + right_depth
        global_max[0] = local_max if global_max[0] < local_max else global_max[0]
        return max(left_depth, right_depth) + 1
