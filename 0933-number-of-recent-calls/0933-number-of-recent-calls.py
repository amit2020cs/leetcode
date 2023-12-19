class RecentCounter:

    def __init__(self):
        self.slide_win = deque()
        

    def ping(self, t: int) -> int:
        self.slide_win.append(t)
        
        while self.slide_win[0] < t- 3000:
            self.slide_win.popleft()
        
        return len(self.slide_win)
        


# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)