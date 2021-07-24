"""
The thief has found himself a new place for his thievery again. There is only one entrance to this area, called root.
Besides the root, each house has one and only one parent house. After a tour, the smart thief realized that all 
houses in this place form a binary tree. It will automatically contact the police if two directly-linked houses were
broken into on the same night.

Given the root of the binary tree, return the maximum amount of money the thief can rob without alerting the police.
@Author: Daniel Mai
"""
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def rob(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        def dfs(root):
            if root == None: return [0,0]
            
            left_amount = dfs(root.left)
            right_amount = dfs(root.right)
            
            withRoot = root.val + left_amount[1] + right_amount[1]
            withoutRoot = max(left_amount) + max(right_amount)
            
            return [withRoot, withoutRoot]
        
        return max(dfs(root))

"""
Runtime: 40 ms, faster than 70.71% of Python online submissions for House Robber III.
Memory Usage: 17.2 MB, less than 98.93% of Python online submissions for House Robber III.
"""
            