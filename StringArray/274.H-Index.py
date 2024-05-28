class Solution(object):
    def hIndex(self, citations):
        """
        :type citations: List[int]
        :rtype: int
        """
        citations.sort()
        n, i = len(citations), 1
        found_h_index = False

        while i <= n and (not found_h_index):
          if citations[n - i] < i: 
            found_h_index = True
          
          if not found_h_index:
            i += 1

        return i - 1
