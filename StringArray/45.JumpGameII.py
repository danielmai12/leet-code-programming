class Solution(object):
    def jump(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        '''
        Solution 1: Dynamic Programming
        n = len(nums)
        dp = [float('inf') for _ in range(n - 1)]
        dp.append(0)

        for i in range(n - 2, -1, -1):
          maxJumpLength = min(nums[i], n - i - 1)
          if maxJumpLength > 0:
            dp[i] = 1 + min(dp[i + 1 : i + maxJumpLength + 1])

        return dp[0]
        '''

        '''
        Two pointers? Sliding window?
        '''
        res = 0
        l, r = 0, 0

        while r < len(nums) - 1:
          farthest = 0

          for i in range(l, r + 1):
            farthest = max(farthest, i + nums[i])
            l += 1
        
          l = r + 1
          r = farthest
          res += 1

        return res
          

        