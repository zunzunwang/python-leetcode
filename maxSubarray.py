from typing import List

'''
Given an integer array nums, find the contiguous subarray (containing at least one number) which has the largest sum and return its sum.

Example:

Input: [-2,1,-3,4,-1,2,1,-5,4],
Output: 6
Explanation: [4,-1,2,1] has the largest sum = 6.
Follow up:

If you have figured out the O(n) solution, try coding another solution using the divide and conquer approach, which is more subtle.
'''
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        previousMax = 0
        result = nums[0]
        for num in nums:
            previousMax = max(num, num + previousMax)
            result = previousMax if previousMax > result else result
        return result

    def maxSubArray2(self, nums:List[int]) -> int:
        if len(nums) == 1:
            return nums[-1]

        mid = len(nums)//2
        lsum = self.maxSubArray2(nums[0: mid])
        rsum = self.maxSubArray2(nums[mid:])

        lmsum = 0
        lmsummax = nums[mid -1]
        for i in range(mid -1, -1, -1):
            lmsum += nums[i]
            lmsummax = max(lmsummax, lmsum)

        rmsum = 0
        rmsummax = nums[mid]
        for i in range(mid, len(nums)):
            rmsum += nums[i]
            rmsummax = max(rmsummax, rmsum)

        return max(lmsummax + rmsummax, max(lsum, rsum))


    def maxSubArray3(self, nums:[List[int]]) -> int:
        if len(nums) == 1:
            return nums[0]
        result = previousMax = nums[0]
        for right in range(1,len(nums)):
            previousMax = max(previousMax + nums[right], nums[right])
            result = max(result, previousMax)
        return result