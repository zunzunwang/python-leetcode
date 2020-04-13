"""
Given a binary array, find the maximum length of a contiguous subarray with equal number of 0 and 1.

Example 1:
Input: [0,1]
Output: 2
Explanation: [0, 1] is the longest contiguous subarray with equal number of 0 and 1.
Example 2:
Input: [0,1,0]
Output: 2
Explanation: [0, 1] (or [1, 0]) is a longest contiguous subarray with equal number of 0 and 1.
Note: The length of the given binary array will not exceed 50,000.


Approach #2 Using Extra Array [Accepted]
Algorithm
每个1 记为 +1
每个0 记为 -1
如果两个相互抵消则会回到相同的起点高度
所以我们需要遍历一遍数组来确定所有的点的高度
如果出现了同一个高度 则更新最大值的距离

注意初始点为 0： -1
"""
from typing import List


class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        d = {0: -1}
        result_max = 0
        base = 0
        for i in range(len(nums)):
            if nums[i] == 1:
                base += 1
            else:
                base -= 1
            if base in d:
                result_max = max(result_max, i - d[base])
            else:
                d[base] = i
        return result_max
