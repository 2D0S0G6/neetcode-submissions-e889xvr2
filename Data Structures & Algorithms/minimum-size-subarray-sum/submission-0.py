from typing import List

class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        min_len = float('inf')
        l = 0
        for r in range(len(nums)):
            # This is still inefficient because sum() is O(n)
            while sum(nums[l:r+1]) >= target:
                min_len = min(min_len, r - l + 1)
                l += 1
        return min_len if min_len != float('inf') else 0