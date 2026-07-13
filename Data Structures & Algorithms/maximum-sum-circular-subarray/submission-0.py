class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        total = sum(nums)
        cur_max = max_sum = nums[0]
        for x in nums[1:]:
            cur_max = max(x,x+cur_max)
            max_sum = max(max_sum,cur_max)
        cur_min = min_sum = nums[0]
        for x in nums[1:]:
            cur_min = min(x,cur_min+x)
            min_sum = min(cur_min,min_sum)
        if max_sum < 0:
            return max_sum
        return max(max_sum,total-min_sum)