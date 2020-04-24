class BinaryMatrix(object):
    def __init__(self, x):
        self.val = x

    def get(self, row: int, col: int) -> int:
        return self.val[row][col]

    def dimensions(self) -> list:
        return [len(self.val), len(self.val[0])]


"""
(This problem is an interactive problem.)

A binary matrix means that all elements are 0 or 1. For each individual row of the matrix, this row is sorted 
in non-decreasing order.

Given a row-sorted binary matrix binaryMatrix, return leftmost column index(0-indexed) with at least a 1 in it. 
If such index doesn't exist, return -1.

You can't access the Binary Matrix directly.  You may only access the matrix using a BinaryMatrix interface:

BinaryMatrix.get(row, col) returns the element of the matrix at index (row, col) (0-indexed).
BinaryMatrix.dimensions() returns a list of 2 elements [rows, cols], which means the matrix is rows * cols.
Submissions making more than 1000 calls to BinaryMatrix.get will be judged Wrong Answer.  Also, any solutions 
that attempt to circumvent the judge will result in disqualification.

For custom testing purposes you're given the binary matrix mat as input in the following four examples. 
You will not have access the binary matrix directly.
"""


class Solution:
    def leftMostColumnWithOne(self, binaryMatrix: 'BinaryMatrix') -> int:
        [r, c] = binaryMatrix.dimensions()
        limit = c - 1
        is_find = False
        for i in range(r):
            if binaryMatrix.get(i, c - 1) == 1:
                is_find = True
                limit = min(self.binary_search(binaryMatrix, limit, i), limit)
                if limit == 0:
                    return limit

        if not is_find:
            return -1
        else:
            return limit

    def binary_search(self, binaryMatrix: 'BinaryMatrix', end: int, row: int) -> int:
        start = 0
        while start <= end:
            mid = start + (end - start) // 2
            if binaryMatrix.get(row, mid) == 0:
                start = mid + 1
            else:
                end = mid - 1
        return start
