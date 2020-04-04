from typing import List

'''
Given an array nums, write a function to move all 0's to the end of it while maintaining the relative order of the non-zero elements.

Example:

Input: [0,1,0,3,12]
Output: [1,3,12,0,0]
Note:

You must do this in-place without making a copy of the array.
Minimize the total number of operations.

交换时都移动， 否则只移动头部指针 
'''
class Solution:

    def moveZeros(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        if len(nums) == 1:
            return

        end = 0
        for head in range(len(nums)):
            if nums[head] != 0:
                nums[head], nums[end] = nums[end], nums[head]
                end += 1
