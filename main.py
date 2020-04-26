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
import last_stone_weight as lsw
import contiguous_array as ca
import perform_string_shifts as pss
import product_of_array_except_self as poaes
import number_of_islands as noi
import minimum_path_sum as mps
import search_in_rotated_sorted_array as sursa
import construct_binary_search_tree_from_preorder_traversal as cbstfpt
import leftmost_column_with_at_least_a_one as lcwalao
import subarray_sum_equals_k as ssek
import bitwise_and_of_numbers_range as baonr
import lru_cache as lc

# day1 single Number
print("day1 single Number")
s = sn.Solution()
print(s.singleNumber([4, 1, 2, 3, 3, 2, 1, 5, 5]))
print('-----------------')

# day2 happyNumber
print("day2 happyNumber")
s = hn.Solution()
print(s.isHappy(2))
print('-----------------')

# day3 maxSubarray
print("day3 maxSubarray")
s = ms.Solution()
print(s.maxSubArray3([21, -100, 20, 80, -500, 90]))
print('-----------------')

# day4 movesZeros
print("day4 movesZeros")
s = mz.Solution()
nums = [0, 1, 0, 3, 12]
s.moveZeros(nums)
print(nums)
print('-----------------')

# day5 best time to buy and sell stock II
print("day5 best time to buy and sell stock II")
s = bttbas2.Solution()
print(s.maxProfit([7, 1, 5, 3, 6, 4]))
print('-----------------')

# day6 group Anagrams
print("day6 group Anagrams")
s = ga.Solution()
dis.dis('{}')
dis.dis('dict()')

print(s.groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"]))
print('-----------------')

# day7 Counting Elements
print("day7 Counting Elements")
s = ce.Solution()
print(s.countElements([1, 3, 2, 3, 5, 0]))
print('-----------------')

# Day8 middle of the linked list
print("Day8 middle of the linked list")
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

# day9 back space string compare
print("day9 back space string compare")
s = bssc.Solution()
print(s.backspaceCompare("###ab#c", "ad#c"))
print(s.backspaceCompare2("###ab#cd", "ad#cc#d"))
print('-----------------')

# day10 min stack
print("day10 min stack")
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
print("day11 diameter of binary tree")
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
print('-----------------')

# day12 last stone weight
print("day12 last stone weight")
s = lsw.Solution()
print(s.lastStoneWeight([6, 7, 8, 8, 9, 9]))
print('-----------------')

# day13 contiguous array
print("day13 contiguous array")
s = ca.Solution()
print(s.findMaxLength([1, 0, 1, 0, 1, 1, 0]))
print('-----------------')

# day14 perform string shifts
print("day14 perform string shifts")
s = pss.Solution()
print(s.stringShift('abcdefg', [[0, 1], [1, 3]]))
print('-----------------')

# day15 product of array except self
print("day15 product of array except self")
s = poaes.Solution()
print(s.productExceptSelf([1, 2, 3, 4]))
print('-----------------')

# day16 Number of Islands
print("day16 Number of Islands")
s = noi.Solution()
print(s.numIslands(
    [["1", "1", "1", "1", "0"], ["1", "1", "0", "1", "0"], ["1", "1", "0", "0", "0"], ["0", "0", "0", "0", "0"]]))
print('-----------------')

# day 17 Minimum Path Sum
print("day17 Minimum Path Sum")
s = mps.Solution()
print(s.minPathSum([[1, 3, 1], [1, 5, 1], [4, 2, 1]]))
print('-----------------')

# day 18 Search in Rotated Sorted Array
print("day18 Search in Rotated Sorted Array")
s = sursa.Solution()
print(s.search([4, 5, 6, 7, 0, 1, 2], 0))
print('-----------------')

# day 19 Construct Binary Search Tree from Preorder Traversal
print("day19 Construct Binary Search Tree from Preorder Traversal")
s = cbstfpt.Solution()
root = s.bstFromPreorder([8, 5, 1, 7, 10, 12])
cbstfpt.bfs_traversal(root)
print('-----------------')

# day 20 Construct Binary Search Tree from Preorder Traversal
print("day20 Leftmost Column with at Least a One")
s = lcwalao.Solution()
obj = lcwalao.BinaryMatrix([[0, 0, 1], [0, 0, 1], [0, 1, 0]])
print(s.leftMostColumnWithOne(obj))
print('-----------------')

# day 21 Subarray Sum Equals K
print("Subarray Sum Equals K")
s = ssek.Solution()
print(s.subarraySum([1, 1, 1, 1], 2))
print('-----------------')

# day 22 Bitwise AND of Numbers Range
print("Bitwise AND of Numbers Range")
s = baonr.Solution()
print(s.rangeBitwiseAnd(5, 7))
print('-----------------')

# day 23  LRU Cache
print("LRU Cache")
obj = lc.LRUCache(2)
print("put 1, 1")
obj.put(1, 1)
print("put 2, 2")
obj.put(2, 2)
print("get 1")
obj.get(1)
print("put 3, 3")
obj.put(3, 3)
print("get 2")
obj.get(2)
print("put 4, 4")
obj.put(4, 4)
print("get 1")
obj.get(1)
print("get 3")
obj.get(3)
print("get 4")
obj.get(4)
print('-----------------')