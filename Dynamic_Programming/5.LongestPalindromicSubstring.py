class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        n = len(s)
        dp = [[False]*n for i in range(n)]
        
        maxLen = -1
        i_longest = 0
        j_longest = 0
        
        for size in range(1, n+1):
            for i in range(n - size + 1):
                j = i + size - 1
                
                if i == j: # Base case 1: size = 1
                    dp[i][j] = True
                
                elif s[i] == s[j]: # Recursive case: first and last words are equal
                    if i + 1 == j: # Base case 2: size = 2
                        dp[i][j] = True
                    else:
                        dp[i][j] = dp[i+1][j-1]
                
            
                if dp[i][j] and j-i>=maxLen:
                    maxLen=j-i
                    i_longest=i
                    j_longest=j
            

        return s[i_longest:j_longest+1]