class Solution(object):
    def canCompleteCircuit(self, gas, cost):
        """
        :type gas: List[int]
        :type cost: List[int]
        :rtype: int
        """

        # https://www.youtube.com/watch?v=xmJZSYSvgfE
        total_diff = 0
        curr_gas = 0
        start_idx = 0

        for i in range(len(gas)):
          curr_gas += gas[i] - cost[i]
          total_diff += gas[i] - cost[i]
          if curr_gas < 0:
            start_idx = i + 1
            curr_gas = 0
          
        return -1 if total_diff < 0 else start_idx
        