from collections import Counter
from operator import itemgetter
from typing import List
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = Counter(nums)
        sorted_d = dict(sorted(freq.items(), key=itemgetter(1), reverse=True))

        return list(sorted_d.keys())[:k]