import collections
from typing import List


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


def bfs_traversal(root: TreeNode):
    if root is None:
        return

    queue = collections.deque()
    queue.append(root)
    while len(queue) > 0:
        node = queue.pop()
        if node is not None:
            if node.left is not None or node.right is not None:
                queue.appendleft(node.left)
                queue.appendleft(node.right)
            print(node.val)
        else:
            print(node)

class Solution:
    def bstFromPreorder2(self, preorder: List[int]) -> TreeNode:
        return self.rebuild_tree(preorder, 1, len(preorder) - 1)

    def rebuild_tree2(self, preorder: List[int], start, end) -> TreeNode:
        root = TreeNode(preorder[start])
        if end == start:
            return root

        for i in range(start + 1, end + 1):
            if preorder[i] > preorder[start]:
                break

        if preorder[i] > preorder[start]:  # find right
            root.right = self.rebuild_tree(preorder, i, end)
            if i > start + 1:  # find left
                root.left = self.rebuild_tree(preorder, start + 1, i - 1)
        else:  # not find right
            root.left = self.rebuild_tree(preorder, start + 1, end)
        return root

    def bstFromPreorder(self, preorder: List[int]) -> TreeNode:
        root = None
        for i in range(len(preorder)):
            root = self.rebuild_tree(root, preorder[i])
        return root

    def rebuild_tree(self, root: TreeNode, val: int) -> TreeNode:
        if root is None:
            return TreeNode(val)

        if root.val > val:
            root.left = self.rebuild_tree(root.left, val)
        else:
            root.right = self.rebuild_tree(root.right, val)
        return root

