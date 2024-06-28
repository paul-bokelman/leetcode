from typing import List

# choose most optimal items to fill knapsack
# procedure: compute 

class Solution:
    def knapsack(self, items: List[tuple[int,int]], capacity: int) -> List[tuple[int, int]]:
        if len(items) == 0:
            return [] 
        
        # store computed values in matrix
        capacity_matrix: List[List[int]] = [[0] * (capacity + 1)]

        # compute capacity matrix
        for item_index in range(1, len(items) + 1):
            value, weight = items[item_index - 1]
            capacity_matrix.append([0] * (capacity + 1))
            for current_capacity in range(capacity + 1):
                # weight is greater than capacity -> use previous
                if weight > current_capacity:
                    capacity_matrix[item_index][current_capacity] = capacity_matrix[item_index - 1][current_capacity]

                # weight is equal to capacity -> choose max of previous value and current value
                if weight == current_capacity:
                    capacity_matrix[item_index][current_capacity] = max(value, capacity_matrix[item_index - 1][current_capacity])

                # weight is less than capacity -> choose current item then shift and add previous capacity 
                if weight < current_capacity:
                    capacity_matrix[item_index][current_capacity] = value + capacity_matrix[item_index - 1][current_capacity - weight]

        optimal_items: List[tuple[int, int]] = []

        # find most optimal items that produced best value
        current_capacity_index = capacity

        for item_index in range(len(items), 0, -1):
            # value isn't equal to value above it -> append item and move indexes
            if capacity_matrix[item_index][current_capacity_index] != capacity_matrix[item_index - 1][current_capacity_index]:
                item = items[item_index - 1]
                optimal_items.append(item)

                current_capacity_index -= item[1] # shift capacity index by weight of selected item
        return optimal_items
    

print(Solution().knapsack([(1,3), (4,3), (8,5), (5,6)], 10))
print(Solution().knapsack([(2,3), (2,1), (4,3), (5,4), (3,2)], 7))