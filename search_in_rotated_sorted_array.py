"""
Suppose an array sorted in ascending order is rotated at some pivot unknown to you beforehand.

(i.e., [0,1,2,4,5,6,7] might become [4,5,6,7,0,1,2]).

You are given a target value to search. If found in the array return its index, otherwise return -1.

You may assume no duplicate exists in the array.

Your algorithm's runtime complexity must be in the order of O(log n).

Example 1:

Input: nums = [4,5,6,7,0,1,2], target = 0
Output: 4
Example 2:

Input: nums = [4,5,6,7,0,1,2], target = 3
Output: -1

此处考察的是二分查找的变形
二分查找的时间复杂度是 O(log n)
此处是要利用边界条件改变的二分查找
每一次查找mid 会分出两个区间
一个单调增和一个非单调增
如果在单调增区间没有找到相应的值，则需要在另一半非单调增区间进行寻找
直到找到结果或者跳出循环
"""
from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums) - 1
        while right >= left:  # 循环的条件一定要带等号
            mid = left + (right - left) // 2  # 计算中点利用减法
            if nums[mid] == target:
                return mid
            elif nums[left] <= nums[mid]:  # 等号对于mid=left的情况
                if nums[left] <= target < nums[mid]:
                    right = mid - 1
                else:
                    left = mid + 1
            else:
                if nums[mid] < target <= nums[right]:
                    left = mid + 1
                else:
                    right = mid - 1
        return -1
