class TimeMap:

    def __init__(self):
        self.store = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.store:
            self.store[key] = []
        self.store[key].append([timestamp, value])
        
    def get(self, key: str, timestamp: int) -> str:
        res = ""
        records = self.store.get(key, [])     

        l, r = 0, len(records) - 1
        while l <= r:
            mid = (l + r) // 2
            if records[mid][0] <= timestamp:  
                res = records[mid][1]         
                l = mid + 1                   
            else:                             
                r = mid - 1                   

        return res
        
