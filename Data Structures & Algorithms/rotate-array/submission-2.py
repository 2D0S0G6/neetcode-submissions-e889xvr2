class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        nums_copy = nums[:]
        for i in range(len(nums)):
            nums[(i+k)%len(nums)] = nums_copy[i] 
        
