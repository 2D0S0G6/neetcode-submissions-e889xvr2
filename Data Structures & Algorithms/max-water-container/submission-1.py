class Solution:
    def maxArea(self, heights: List[int]) -> int:
        left = 0
        right = len(heights)-1
        max_cap = 0
        while left < right:
            width = right -  left
            container_height = min(heights[left],heights[right])
            area = width * container_height
            max_cap = max(area,max_cap)
            if heights[left] < heights[right]:
                left+=1
            else:
                right-=1
        return max_cap