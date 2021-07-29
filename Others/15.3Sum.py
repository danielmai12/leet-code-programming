"""
Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that 
i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.

Notice that the solution set must not contain duplicate triplets.
"""
class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        results = []
        
        sort_nums = sorted(nums)
        for i in range(len(sort_nums)):
            first_num = sort_nums[i]
            
            if i > 0 and first_num == sort_nums[i-1]:
                continue
                
            L_pointer, R_pointer = i+1, len(sort_nums) - 1
            
            while L_pointer < R_pointer:
                three_sum = first_num + sort_nums[L_pointer] + sort_nums[R_pointer]
                
                if three_sum < 0: # -> Move the L_pointer to the right
                    L_pointer += 1
                elif three_sum > 0: # -> Move the R_pointer to the left
                    R_pointer -= 1
                else: # three_sum = 0 -> add this three numbers to the results list
                    results.append( [first_num, sort_nums[L_pointer], sort_nums[R_pointer]] )            
                    L_pointer += 1
                    while sort_nums[L_pointer] == sort_nums[L_pointer - 1] and L_pointer < R_pointer:
                        L_pointer +=1
        
        return results
    
"""
Runtime: 648 ms, faster than 81.49% of Python online submissions for 3Sum.
Memory Usage: 16.8 MB, less than 49.41% of Python online submissions for 3Sum.
"""