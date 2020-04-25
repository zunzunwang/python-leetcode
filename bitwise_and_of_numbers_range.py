"""
Given a range [m, n] where 0 <= m <= n <= 2147483647, return the bitwise AND of all numbers in this range, inclusive.

Example 1:

Input: [5,7]
Output: 4
Example 2:

Input: [0,1]
Output: 0

只要发现一个高位的值不同， 则可以确定低位是一定被置零的
0 1 1 1
1 0 0 0
所以只需要找到最高位相同的即可
其他后面的高位都保留
"""
class Solution:
    def rangeBitwiseAnd(self, m: int, n: int) -> int:
        count = 0
        while m != n:
            # 进行右移比较
            m >>= 1
            n >>= 1
            count += 1
        # rebuild the origin bit
        return m << count

