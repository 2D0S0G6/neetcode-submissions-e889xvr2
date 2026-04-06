class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        if not intervals:
            return 0
        
        starts = sorted(i.start for i in intervals)
        ends = sorted(i.end for i in intervals)
        
        rooms = 0
        max_rooms = 0
        i = j = 0
        
        while i < len(intervals):
            if starts[i] < ends[j]:
                rooms += 1
                max_rooms = max(max_rooms, rooms)
                i += 1
            else:
                rooms -= 1
                j += 1
        
        return max_rooms