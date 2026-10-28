# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        self.equivalent = True

        def equal(a, b):
            if not a and not b:          
                return
            if not a or not b:          
                self.equivalent = False
                return
            if a.val != b.val:           
                self.equivalent = False
                return
            equal(a.left, b.left)        
            equal(a.right, b.right)     

        equal(p, q)
        return self.equivalent
                
            