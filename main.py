import singleNumber as sn
import happyNumber as hn
import maxSubarray as ms
import movesZeros as mz

#day1 single Number
s = sn.Solution()
print(s.singleNumber([4,1,2,3,3,2,1,5,5]))
print('-----------------')

#day2 happyNumber
s = hn.Solution()
print(s.isHappy(2))
print('-----------------')

#day3 maxSubarray
s = ms.Solution()
print(s.maxSubArray3([21,-100,20,80,-500,90]))
print('-----------------')

#day4 movesZeros
s = mz.Solution()
nums = [0,1,0,3,12]
s.moveZeros(nums)
print(nums)