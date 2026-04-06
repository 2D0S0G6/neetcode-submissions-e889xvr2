class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        res = max(nums)
        curMin, curMax = 1, 1

        for n in nums:
            if n == 0:
                curMin, curMax = 1, 1
                continue

            tmpMax = curMax * n
            tmpMin = curMin * n

            curMax = max(tmpMax, tmpMin, n)
            curMin = min(tmpMax, tmpMin, n)

            res = max(res, curMax)

        return res