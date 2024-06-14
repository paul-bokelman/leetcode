from typing import List, Set

class Solution:
    def nearestExit(self, maze: List[List[str]], entrance: List[int]) -> int:
        max_width = len(maze[0]) - 1 # right-most index of maze
        max_height = len(maze) - 1 # bottom index of maze
        queue = [(entrance[1], entrance[0])]
        visited: Set[tuple[int, int]] = set() # store coordinate points
        level = 0
        nodesBeforeIncrease = 0


        # iterate through queue until solution is reached or all nodes visited
        while len(queue) > 0:
            (x, y) = queue.pop(0) # get top node in queue
            visited.add((x, y)) # add to list of visited nodes
            if (x == 0 or y == 0 or x == max_width or y == max_height): # check if solution (position is on border)
                return level if level > 0 else -1 # make sure entrance wasn't solution
            

            #todo: calculate distance from origin and check if longer than level
            
            # push all valid adjacent children (not outside, not visited, and open spot)

            # left adjacent
            left = (x - 1, y)
            if left[0] >= 0 and left not in visited and maze[left[1]][left[0]] != "+": 
                queue.append(left)

            # right adjacent
            right = (x + 1, y)
            if right[0] <= max_width and right not in visited and maze[right[1]][right[0]] != "+": 
                queue.append(right)

            # top adjacent
            top = (x, y + 1)
            if top[0] >= 0 and top not in visited and maze[top[1]][top[0]] != "+": 
                queue.append(top)

            # bottom adjacent
            bottom = (x, y - 1)
            if bottom[0] <= max_height and bottom not in visited and maze[bottom[1]][bottom[0]] != "+": 
                queue.append(bottom)
            
        return -1
    
print(Solution().nearestExit([["+","+",".","+"],
                              [".",".",".","+"],
                              ["+","+","+","."]], [1,2]))
print(Solution().nearestExit([[".","+"]], [0,0]))
print(Solution().nearestExit([["+","+","+"],
                              [".",".","."],
                              ["+","+","+"]], [1,0]))