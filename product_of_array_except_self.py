"""
Given an array nums of n integers where n > 1,
return an array output such that output[i] is equal to the product of all the elements of nums except nums[i].

Example:

Input:  [1,2,3,4]
Output: [24,12,8,6]
Constraint: It's guaranteed that the product of the elements of any prefix or suffix of the array
(including the whole array) fits in a 32 bit integer.

Note: Please solve it without division and in O(n).

Follow up:
Could you solve it with constant space complexity? (The output array does not count as extra space for the purpose of
space complexity analysis.)

不能使用除法。 巧妙的使用一个（或者）两个数组来记录
| 1 | 2 | 3 | 4 | 5 |
| 1 | 1 | 2 | 6 |24 | 这一行记录的为所有元素左边元素的乘积
|24 |24 |12 | 4 | 1 | 这一行记录的为所有元素右边元素的乘积

也可以使用tmp来代替存储 直接进行相乘处理
"""
from typing import List


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        out_put_arr = [1]
        tmp = 1
        for i in range(len(nums) - 1):
            out_put_arr.append(out_put_arr[-1] * nums[i])
        for i in range(len(nums) - 1, -1, -1):
            out_put_arr[i] *= tmp
            tmp *= nums[i]
        return out_put_arr
