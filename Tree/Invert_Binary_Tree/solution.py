# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if root == None:
            return None
        elif root.left == None and root.right == None:
            return root
        elif root.left == None:
            return TreeNode(val = root.val, left = self.invertTree(root.right))
        elif root.right == None:
            return TreeNode(val = root.val, right = self.invertTree(root.left))
        else:
            return TreeNode(val = root.val, left = self.invertTree(root.right), right = self.invertTree(root.left))
        
    def print_in_order(self, tree):
        if tree == None:
            return
        if tree.left == None and tree.right == None:
            print(tree.val)
        else:
            self.print_in_order(tree.left)
            print(tree.val)
            self.print_in_order(tree.right)

if __name__ == '__main__':
    s1 = TreeNode(3)
    t = TreeNode(2, right=s1)
    s = Solution()
    t1 = s.invertTree(t)
    print(t1.val == 2)
    print(t1.left.val == 3)
