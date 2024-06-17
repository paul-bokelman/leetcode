from collections import deque

# https://leetcode.com/problems/number-of-recent-calls/?envType=study-plan-v2&envId=leetcode-75
class RecentCounter:
    # use a queue and just remove last
    def __init__(self):
        #/ using a deque (fast list appends and either end pops) to greatly increase efficiency
        #/ other approach required slicing list whereas deque only requires item quick removal
        self.q = deque()

    def ping(self, t: int) -> int:
        # add to request list
        self.q.append(t)

        # mutate queue to reflect number of valid requests 
        while self.q and self.q[0] < t - 3000:
            self.q.popleft() 

        return len(self.q)

    # slower time complexity approach 
    def __init__Slower(self):
        self.requests = []

    def pingSlower(self, t: int) -> int:
        lower_bound = t - 3000

        # add to request list
        self.requests.append(t)

        # mutate list to only include requests in range
        lower_index = -1

        for (index, request) in enumerate(self.requests):
            # get lower index
            if request >= lower_bound and lower_index == -1:
                lower_index = index

        self.requests = self.requests[lower_index:]

        return len(self.requests)


    
counter = RecentCounter()
counter.ping(1) # requests = [1], range is [-2999,1], return 1
counter.ping(100) # requests = [1, 100], range is [-2900,100], return 2
counter.ping(3001) # requests = [1, 100, 3001], range is [1,3001], return 3
counter.ping(3002) # requests = [1, 100, 3001, 3002], range is [2,3002], return 3

print(counter.requests)