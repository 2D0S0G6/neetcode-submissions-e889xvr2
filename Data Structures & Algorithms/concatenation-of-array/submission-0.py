class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        ans = []
        n = len(nums)
        i = 0
        while len(ans) < 2*n :
            ans.append(nums[i])
            i = (i+1)%n
        return ans
            