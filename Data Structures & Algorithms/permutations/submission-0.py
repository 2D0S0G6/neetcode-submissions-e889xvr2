class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:        
        res = []
        cur = []
        freq = Counter(nums)

        def dfs():
            if len(cur) == len(nums):
                res.append(cur.copy())
                return

            for num in freq:
                if freq[num] > 0:
                    cur.append(num)
                    freq[num] -= 1
                    dfs()
                    cur.pop()
                    freq[num] += 1

        dfs()
        return res
