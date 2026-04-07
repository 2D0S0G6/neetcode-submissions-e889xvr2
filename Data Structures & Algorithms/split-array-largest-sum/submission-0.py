class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        def canSplit(largest):
            subarray = 1
            cur_sum = 0
            for num in nums:
                cur_sum += num
                if cur_sum > largest:
                    subarray += 1
                    if subarray > k:
                        return False
                    cur_sum = num
            return True

        l,r = max(nums),sum(nums)
        res = r
        while l <= r :
            mid = l +(r-l)//2
            if canSplit(mid):
                res = mid
                r = mid-1
            else :
                l = mid+1
        return res
                     