import singleNumber as sn
import happyNumber as hn
import maxSubarray as ms
import movesZeros as mz
import bestTimeToBuyAndSellStockII as bttbas2
import groupAnagrams as ga
import dis
import countingElements as ce
import middleOfTheLinkedList as motll
import backspaceStringCompare as bssc
import minStack as mstack
import diameter_of_binary_tree as dobt

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

print(s.groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"]))
print('-----------------')

# day7 Counting Elements
s = ce.Solution()
print(s.countElements([1, 3, 2, 3, 5, 0]))
print('-----------------')

# Day8 middle of the linked list
s = motll.Solution()
n1 = motll.ListNode(1)
n2 = motll.ListNode(2)
n3 = motll.ListNode(3)
n4 = motll.ListNode(4)
n5 = motll.ListNode(5)
n1.next = n2
n2.next = n3
n3.next = n4
n4.next = n5
result = s.middleNode(n1)
while result:
    print(result.val)
    result = result.next
print('-----------------')

# Day9 back space string compare
s = bssc.Solution()
print(s.backspaceCompare("###ab#c", "ad#c"))
print(s.backspaceCompare2("###ab#cd", "ad#cc#d"))
print('-----------------')

# day10 min stack
minStack = mstack.MinStack()
minStack.push(4)
minStack.push(5)
minStack.push(6)
minStack.push(3)
print(minStack.getMin())
minStack.pop()
print(minStack.top())
print(minStack.getMin())
print('-----------------')

# day11 diameter of binary tree
"""
          1
         / \
        2   3
       / \     
      4   5    
"""
n1 = dobt.TreeNode(1)
n2 = dobt.TreeNode(2)
n3 = dobt.TreeNode(3)
n4 = dobt.TreeNode(4)
n5 = dobt.TreeNode(5)
n1.left = n2
n1.right = n3
n2.left = n4
n2.right = n5
s = dobt.Solution()
print(s.diameterOfBinaryTree(n1))