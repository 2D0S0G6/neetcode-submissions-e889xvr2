class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        L_max = []
        dq = deque()
        left = 0
        cur_max = 0
        for right in range(len(nums)):
            while dq and nums[dq[-1]] < nums[right]:
                dq.pop()

            dq.append(right)

            if dq[0] < left:
                dq.popleft()
            if (right - left + 1) == k :
                L_max.append(nums[dq[0]])
                left += 1
        return L_max
            
