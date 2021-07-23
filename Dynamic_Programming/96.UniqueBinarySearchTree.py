# Given an integer n, return the number of structurally unique BST's (binary search trees) which has exactly n nodes of unique values from 1 to n.

class Solution(object):
    def numTrees(self, n):
        """
        :type n: int
        :rtype: int
        """
        dp = [0] * (n+1) # table to store all the number of unique BST for key i=0,1,2,...,n
        
        # Base case.
        dp[0] = 1
        dp[1] = 1
        
        for i in range(2, n+1):
            for j in range(0, i):
                dp[i] += dp[i-j-1] * dp[j] 
                
        return dp[n]
    

# Runtime: 20 ms, faster than 48.04% of Python online submissions for Unique Binary Search Trees.
# Memory Usage: 13.3 MB, less than 62.01% of Python online submissions for Unique Binary Search Trees.