class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total_sum = sum(nums)
        
        if total_sum % 2 != 0:
            return False
        
        target = total_sum // 2
        
        dp = set()
        dp.add(0)
        for i in range(len(nums)-1,-1,-1):
            nextDP = set()
            for t in dp:
                nextDP.add(t+nums[i])
                nextDP.add(t)

                dp = nextDP
        return True if target in dp else False