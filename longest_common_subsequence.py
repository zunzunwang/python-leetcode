"""
首先一个给定长度为n的序列，他的所有子序列subsequence 有2^n个（每个元素有可能出现或者不出现所以2个可能性）
如果去比较一个序列是否是另一个的子集， 复杂度为O(n).
先比较第一个元素然后在子串比较第二个元素以此类推
"""


class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        x = len(text1)
        y = len(text2)

        matrix = [[None] * (x + 1) for i in range(y + 1)]

        # set the value of the matrix
        for i in range(y + 1):
            for j in range(x + 1):
                if i == 0 or j == 0:  # init the first line and first column
                    matrix[i][j] = 0
                elif text1[j-1] == text2[i-1]:
                    matrix[i][j] = matrix[i-1][j-1] + 1
                else:
                    matrix[i][j] = max(matrix[i - 1][j], matrix[i][j - 1])
        return matrix[-1][-1]
