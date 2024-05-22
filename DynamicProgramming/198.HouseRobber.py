"""
You are a professional robber planning to rob houses along a street. Each house has a certain amount of money stashed, 
the only constraint stopping you from robbing each of them is that adjacent houses have security systems connected and 
it will automatically contact the police if two adjacent houses were broken into on the same night.

Given an integer array nums representing the amount of money of each house, return the maximum amount of money you can rob tonight without alerting the police.
"""

class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        
        opt = [0] * n
        
        opt[0] = nums[0]
        
        if n > 1: opt[1] = max(nums[0], nums[1])

        for i in range(2, n):
            # Case 1: The house at pos ith is picked -> num[i] + opt[i-2]
            # Case 2: The house at pos is not picked -> get the optimal solution at pos i-1
            # Choose the maximum between them.
            opt[i] = max(nums[i] + opt[i-2], opt[i-1])
            
        return opt[n-1]

"""        
Runtime: 16 ms, faster than 84.44% of Python online submissions for House Robber.
Memory Usage: 13.4 MB, less than 40.99% of Python online submissions for House Robber.
"""