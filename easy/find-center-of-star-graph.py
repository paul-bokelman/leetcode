# https://leetcode.com/problems/find-center-of-star-graph/?envType=daily-question&envId=2024-06-27
from typing import List

class Solution:
    def findCenter(self, edges: List[List[int]]) -> int:
        connections = {}

        # count connections
        for edge in edges:
            u, v = edge
            if u not in connections:
                connections[u] = 0
            if v not in connections:
                connections[v] = 0
            if u in connections:
                connections[u] += 1
            if v in connections:
                connections[v] += 1

        # find number of connections that center has (n-1)
        center_connections_count = len(connections) - 1

        # find that entry in connections and return key
        for (node, count) in connections.items():
            if count == center_connections_count:
                return node
            
        return -1 

print(Solution().findCenter([[1,2],[2,3],[4,2]]))
print(Solution().findCenter([[1,2],[5,1],[1,3],[1,4]]))
        