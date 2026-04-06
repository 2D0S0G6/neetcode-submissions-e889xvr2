class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        freq_elem = Counter(nums)
        res = []
        for num,count in freq_elem.items():
            if count > len(nums)//3:
                res.append(num)
        return res