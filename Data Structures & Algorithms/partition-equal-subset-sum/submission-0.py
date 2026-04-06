class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total_sum = sum(nums)
        
        if total_sum % 2 != 0:
            return False
        
        target = total_sum // 2
        
        def dfs(index, current_sum):
            if current_sum == target:
                return True
            if current_sum > target or index >= len(nums):
                return False
            return (dfs(index + 1, current_sum + nums[index]) or 
                    dfs(index + 1, current_sum))
        
        return dfs(0, 0)