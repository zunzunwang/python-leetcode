import singleNumber as sn
import happyNumber as hn
import maxSubarray as ms
import movesZeros as mz
import bestTimeToBuyAndSellStockII as bttbas2
import groupAnagrams as ga
import dis

# day1 single Number
s = sn.Solution()
print(s.singleNumber([4, 1, 2, 3, 3, 2, 1, 5, 5]))
print('-----------------')

# day2 happyNumber
s = hn.Solution()
print(s.isHappy(2))
print('-----------------')

# day3 maxSubarray
s = ms.Solution()
print(s.maxSubArray3([21, -100, 20, 80, -500, 90]))
print('-----------------')

# day4 movesZeros
s = mz.Solution()
nums = [0, 1, 0, 3, 12]
s.moveZeros(nums)
print(nums)
print('-----------------')

# day5 best time to buy and sell stock II
s = bttbas2.Solution()
print(s.maxProfit([7, 1, 5, 3, 6, 4]))
print('-----------------')

# day6 group Anagrams
s = ga.Solution()
dis.dis('{}')
dis.dis('dict()')

print(s.groupAnagrams(["eat","tea","tan","ate","nat","bat"]))
print('-----------------')