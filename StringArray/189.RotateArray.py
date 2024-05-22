class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        k = k % len(nums) # make sure k is in bound

        # [1,2,3,4,5,6,7] -> [7, 6, 5, 4, 3, 2, 1], k = 3
        self.reverseList(nums, 0, len(nums) - 1)
        
        # [7, 6, 5, 4, 3, 2, 1] -> [5, 6, 7, 4, 3, 2, 1], k = 3
        self.reverseList(nums, 0, k - 1)

        # [5, 6, 7, 4, 3, 2, 1] -> [5, 6, 7, 1, 2, 3, 4], k = 3
        self.reverseList(nums, k, len(nums) - 1)
        
    def reverseList(self, nums, left, right):
        while left < right:
            nums[left], nums[right] = nums[right], nums[left]
            left += 1
            right -= 1


