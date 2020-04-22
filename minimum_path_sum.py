from typing import List

"""
Given a m x n grid filled with non-negative numbers, find a path from top left to bottom right which minimizes the sum of all numbers along its path.

Note: You can only move either down or right at any point in time.

Example:

Input:
[
  [1,3,1],
  [1,5,1],
  [4,2,1]
]
Output: 7
Explanation: Because the path 1→3→1→1→1 minimizes the sum.
注意这里不能使用递归因为会计算很多次重复制的点
所以使用循环把所有点的可能性都算出来
最左列： 从上面下来
最上行： 从左边来
中间： 比较两者取一个小的
"""


class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if i == 0 and j == 0:
                    continue
                elif i - 1 < 0:  # top row
                    grid[i][j] = grid[i][j - 1] + grid[i][j]
                elif j - 1 < 0:  # left column
                    grid[i][j] = grid[i - 1][j] + grid[i][j]
                else:
                    grid[i][j] = min(grid[i][j - 1], grid[i - 1][j]) + grid[i][j]
        return grid[-1][-1]
