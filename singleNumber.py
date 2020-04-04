from typing import List

'''
Given a non-empty array of integers, every element appears twice except for one. Find that single one.

Note:

Your algorithm should have a linear runtime complexity. Could you implement it without using extra memory?

Example 1:

Input: [2,2,1]
Output: 1
Example 2:

Input: [4,1,2,1,2]
Output: 4

-----------------------------------------------------------------
Test points：
1.linear runtime complexity
2.without extra memory
3.XOR operator: ^

review:
按位异或运算符^
按位异或运算符， 参与运算的两个值， 如果两个响应位相同，则结果为零，如果不同则为一。
a^0 = a
a^1 = 自身取反

特征
按位异或可以使特定的位翻转
对10100001的第二位和第三位进行翻转，可以采用将数字与00000110进行^。

a^a = 0
a^b^b = a
变化-数值的交换
a = a^b
b = b^a
a = a^b
'''


class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        result = 0
        for num in nums:
            result ^= num
        return result


