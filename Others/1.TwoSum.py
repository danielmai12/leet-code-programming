"""
Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.

 
"""
class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        dict_nums = {}
        
        for i in range(len(nums)):
            anotherNum = target - nums[i]
            
            if anotherNum in dict_nums:
                return [i, dict_nums[anotherNum]]
            else:
                dict_nums[nums[i]] = i
                
        