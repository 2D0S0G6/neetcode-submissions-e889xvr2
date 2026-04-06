class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1:
            return nums[0]

        # case 1: rob houses 0 to n-2
        rob1, rob2 = 0, 0
        for i in range(n - 1):
            temp = max(nums[i] + rob1, rob2)
            rob1 = rob2
            rob2 = temp
        case1 = rob2

        # case 2: rob houses 1 to n-1
        rob1, rob2 = 0, 0
        for i in range(1, n):
            temp = max(nums[i] + rob1, rob2)
            rob1 = rob2
            rob2 = temp
        case2 = rob2

        return max(case1, case2)