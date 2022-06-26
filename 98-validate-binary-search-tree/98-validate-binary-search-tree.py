# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque


class Solution:
    
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        return self.solution(root)
        # print(root)
        
    def solution(self, node, lower=float('-inf'), upper=float('inf')):
        
        if node is None:
            return True
        if lower < node.val < upper:
            return self.solution(node.left, lower, node.val) and self.solution(node.right, node.val, upper)
        else:
            return False
        

    
            
            

        
        
        
        
        
                
        
        
        
        
        