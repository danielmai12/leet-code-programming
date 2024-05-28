class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        slow, fast = 0, 0
        
        while fast < len(nums):
          count = 1
          while fast + 1 < len(nums) and nums[fast] == nums[fast + 1]:
            count += 1
            fast += 1

          for i in range(min(2, count)):
            nums[slow] = nums[fast]
            slow += 1

          fast += 1

        return slow
