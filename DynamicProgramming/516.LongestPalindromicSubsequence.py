class Solution(object):
    def longestPalindromeSubseq(self, s):
        """
        :type s: str
        :rtype: int
        """
        n = len(s)
        subprobSols = [[0]*n for i in range(n)] # Create a table for bottom-up DP
        
        for size in range(1, n+1): # fill table from smallest subproblems size to largest
            for i in range(n-size+1):
                j = i + size - 1 # value of j is determined using size of subproblems and current value of i
                
                
                if i == j: # Base case: array of size 1
                    subprobSols[i][j] = 1
                    
                elif s[i] == s[j]: # first recursive case: first and last word are equal
                    if j == i + 1:
                        subprobSols[i][j] = 2
                    else:
                        subprobSols[i][j] = subprobSols[i+1][j-1] + 2 
                        
                else: # second recursive case: first and last words are not equal
                    subprobSols[i][j] = max(subprobSols[i][j-1], subprobSols[i+1][j])
                        
        return subprobSols[0][n-1]