# https://leetcode.com/problems/equal-row-and-column-pairs/
from typing import List

class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        rows_and_columns = {}

        current_row = ()
        for row in grid:
            for col in row:
                current_row += (col,)
            if rows_and_columns.get(current_row, None) is None:
                rows_and_columns[current_row] = 0
            else:
                rows_and_columns[current_row] += 1
            current_row = ()

        current_col = ()
        for i in range(len(grid)):
            for row in grid:
                current_col += (row[i], )
            if rows_and_columns.get(current_col, None) is None:
                rows_and_columns[current_col] = 0
            else:
                rows_and_columns[current_col] += 1
            current_col = ()

        print(rows_and_columns)


        return sum(c for c in rows_and_columns.values() if c != 0)
    
print(Solution().equalPairs([[3,2,1],[1,7,6],[2,7,7]]))
print(Solution().equalPairs([[3,1,2,2],[1,4,4,5],[2,4,2,2],[2,4,2,2]]))
print(Solution().equalPairs([[13,13],[13,13]]))