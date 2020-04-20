from typing import List

"""
Given a 2d grid map of '1's (land) and '0's (water), count the number of islands. An island is surrounded by water and 
is formed by connecting adjacent lands horizontally or vertically. You may assume all four edges of the grid are all 
surrounded by water.

需要注意的是在搜索的时候要往同时4个方向进行搜索
否则会遗漏
"""


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        count = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == "1":
                    count += 1
                    self.clean_points(grid, i, j)
        return count

    def clean_points(self, grid: List[List[str]], i: int, j: int):
        grid[i][j] = 0
        # search up
        if 0 <= i - 1 and grid[i - 1][j] == "1":
            self.clean_points(grid, i - 1, j)
        # search down
        if i + 1 < len(grid) and grid[i + 1][j] == "1":
            self.clean_points(grid, i + 1, j)
        # search left
        if 0 <= j - 1 and grid[i][j - 1] == "1":
            self.clean_points(grid, i, j - 1)
        # search right
        if j + 1 < len(grid[0]) and grid[i][j + 1] == "1":
            self.clean_points(grid, i, j + 1)
