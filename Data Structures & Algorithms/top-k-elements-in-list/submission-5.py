class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        data = Counter(nums)
        arr = []
        sorted_data = dict(sorted(data.items(), key=lambda item: item[1], reverse=True))
        return list(sorted_data.keys())[:k]