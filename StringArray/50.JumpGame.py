class Solution(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """

        """
        Solution 1: O(n^2) - dynamic programming
        n = len(nums)
        dp = [False for _ in range(n - 1)]
        dp.append(True)

        for i in range(n - 2, -1, -1):
          if nums[i] > 0:
            dp[i] = any(dp[i + j] for j in range(1, min(nums[i] + 1, n - i)))

        return dp[0]
        """

        '''
        Greedy approach: 
          - If we can reach the end goal, can we reach the previous index of the end goal?
          - Ex: [2, 3, 1, 1, 4]
            - Initially, goal is 4 (last index).
            - Now we check index 3, can we reach the current goal from this index?
              - Yes, set goal to 3.
              - Keep going.
          - Question: Why we just check the previous index of the current goal (current index)?
            - Reason: If there is another index that can jump to the current goal but far away from current goal.
                      Then it is indeed can jump to the previous index (curr Index - 1).
        '''
        goal = len(nums) - 1

        for i in range(len(nums) - 2, -1, -1):
          if i + nums[i] >= goal:
            goal = i
        
        return goal == 0            

