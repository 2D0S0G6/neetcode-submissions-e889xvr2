class Solution:
    def countBits(self, n: int) -> List[int]:
        res = []
        for num in range(n+1):
            one = 0
            for j in range(32):
                if num & (1 << j):
                    one += 1
            res.append(one)
        return res