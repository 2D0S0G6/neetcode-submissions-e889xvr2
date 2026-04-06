class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        Ctr = Counter(nums)
        for key in Ctr:
            if Ctr[key] > 1:
                return key