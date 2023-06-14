# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:

    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        diameters = []
        self.save_diameter_of_each_node(root, diameters)
        return max(diameters)
    
    def save_diameter_of_each_node(self, tree: Optional[TreeNode], diameters: list[int]):
        if (tree == None):
            return
        else:
            self.save_diameter_of_each_node(tree.left, diameters)
            self.save_diameter_of_each_node(tree.right, diameters)
            diameters.append(2 + self.height_of_binary_tree(tree.left) + self.height_of_binary_tree(tree.right))
    
    def height_of_binary_tree(self, tree : Optional[TreeNode]) -> int:
        if (tree == None):
            return -1
        else:
            return 1 + max(self.height_of_binary_tree(tree.right), self.height_of_binary_tree(tree.left))
    

if __name__ == '__main__':
    t1 = TreeNode(4)
    t3 = TreeNode(7)
    t2 = TreeNode(5, left=t1)
    t = TreeNode(2, left=t1, right=t2)
    s = Solution()
    print(s.diameterOfBinaryTree(t))
