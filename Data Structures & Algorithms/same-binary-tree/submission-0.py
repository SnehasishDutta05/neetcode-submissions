# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if p is None and q is None:
            return True
        if p and q:
            if p.val == q.val :
                check1 = True
            else:
                check1 = False
            
            check2 = self.isSameTree(p.left , q.left)
            check3 = self.isSameTree(p.right , q.right)
            if check1 and check2 and check3:
                return True 
            else:
                return False
        elif p or q:
            return False

            
        


        