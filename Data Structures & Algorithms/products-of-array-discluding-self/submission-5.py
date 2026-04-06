class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        L = []
        for i in range(len(nums)):
            right = i+1
            left = i-1
            r_s = 1
            l_s = 1
            for l in range(0,left+1):
                l_s = l_s*nums[l]
            for r in range(right,len(nums)):
                r_s = r_s*nums[r]
            L.append(r_s*l_s)
        return L

