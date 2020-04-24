import collections
from typing import List

"""
Given an array of integers and an integer k, you need to find the total number of continuous subarrays whose sum equals to k.

Example 1:
Input:nums = [1,1,1], k = 2
Output: 2
Note:
The length of the array is in range [1, 20,000].
The range of numbers in the array is [-1000, 1000] and the range of the integer k is [-1e7, 1e7].

每两个点之间的和的差值 刚好等于所要的值
只需要计算总数列中一共这样有相同和值的点出现过几次
[...13...13...17]如果此时差值为4 则对于前两个点都是满足的
利用dict来记录每个和值出现的次数

"""
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        map_sum = collections.defaultdict(int)
        map_sum[0] = 1
        sum_nums = 0
        count = 0
        for i in range(len(nums)):
            sum_nums += nums[i]
            if sum_nums - k in map_sum:
                count += map_sum[sum_nums - k]
            map_sum[sum_nums] += 1
        return count



