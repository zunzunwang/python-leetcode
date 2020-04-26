from typing import List


class Solution:
    def canJump(self, nums: List[int]) -> bool:
        max_step = 0
        i = 0
        while i <= max_step:
            max_step = max(i + nums[i], max_step)
            if max_step >= len(nums) - 1:
                return True
            i += 1
        return False
