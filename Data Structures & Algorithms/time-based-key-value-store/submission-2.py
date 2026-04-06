class TimeMap:

    def __init__(self):
        self.store = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.store:
            self.store[key]=[]
        self.store[key].append((value,timestamp))


    def get(self, key: str, timestamp: int) -> str:
        if key not in self.store:
            return ""
        arr = self.store[key]
        left,right = 0,len(arr)-1
        res = ""
        while left <= right:
            mid = (left+right)//2
            mid_time = arr[mid][1]
            if mid_time <= timestamp:
                res = arr[mid][0]
                left = mid+1
            else:
                right = mid -1
        return res