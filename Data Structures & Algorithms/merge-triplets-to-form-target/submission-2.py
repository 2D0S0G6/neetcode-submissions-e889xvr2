class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        curr = [0, 0, 0]

        for t in triplets:
            # check if triplet is valid (doesn't exceed target)
            valid = True
            for i in range(3):
                if t[i] > target[i]:
                    valid = False
                    break

            if valid:
                for i in range(3):
                    if t[i] > curr[i]:
                        curr[i] = t[i]

        # final check
        for i in range(3):
            if curr[i] != target[i]:
                return False
        return True
