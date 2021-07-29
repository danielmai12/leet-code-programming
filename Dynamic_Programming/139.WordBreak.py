"""
Given a string s and a dictionary of strings wordDict, return true if s can be segmented into a 
space-separated sequence of one or more dictionary words.

Note that the same word in the dictionary may be reused multiple times in the segmentation.
"""

class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: bool
        """
        n = len(s)
        dp = [False] * (n + 1) # table that will show if the substring from [0:i] can be segmented into a space-seperated sequence of one or more dictionary words or not.
        dp[0] = True
        
        for i in range(1, n+1): # check each pos from the beginning
            for j in range(i): # check each substring.
                if dp[j] and s[j:i] in wordDict: # case when dp[j] is true and the rest is in the wordDict -> dp[i] is true
                    dp[i] = True
                    break
                    
        return dp[n]
        
"""
Runtime: 36 ms, faster than 34.32% of Python online submissions for Word Break.
Memory Usage: 13.4 MB, less than 99.37% of Python online submissions for Word Break.
"""