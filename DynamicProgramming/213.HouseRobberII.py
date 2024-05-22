"""
You are a professional robber planning to rob houses along a street. Each house has a certain amount of money stashed. 
All houses at this place are arranged in a circle. That means the first house is the neighbor of the last one. 
Meanwhile, adjacent houses have a security system connected, 
and it will automatically contact the police if two adjacent houses were broken into on the same night.

Given an integer array nums representing the amount of money of each house, return the maximum amount of money you can rob tonight without alerting the police.

"""

class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        def rob1(nums):
            n = len(nums)

            opt = [0] * n

            opt[0] = nums[0]


            if n > 1: opt[1] = max(nums[0], nums[1])

            for i in range(2, n):
                opt[i] = max(opt[i-1], nums[i] + opt[i-2])

            return opt[n-1]
        
        if len(nums) == 1: return nums[0]
        
        return max( rob1(nums[1:]), rob1(nums[:-1]) )

"""
Runtime: 16 ms, faster than 88.70% of Python online submissions for House Robber II.
Memory Usage: 13.3 MB, less than 69.49% of Python online submissions for House Robber II.
"""