import collections
from typing import List
'''
Given an array of strings, group anagrams together.

Example:

Input: ["eat", "tea", "tan", "ate", "nat", "bat"],
Output:
[
  ["ate","eat","tea"],
  ["nat","tan"],
  ["bat"]
]
Note:

All inputs will be in lowercase.
The order of your output does not matter.


review

pthon 创建 dict的两种方式
d = {}
  1           0 BUILD_MAP                0
              2 RETURN_VALUE
              
d = dict()
  1           0 LOAD_NAME                0 (dict)
              2 CALL_FUNCTION            0
              4 RETURN_VALUE

defaultdict接受一个工厂函数作为参数，如下来构造：

dict =defaultdict( factory_function)
这个factory_function可以是list、set、str等等，作用是当key不存在时，返回的是工厂函数的默认值，比如list对应[ ]，str对应的是空字符串，set对应set( )，int对应0，如下举例：
from collections import defaultdict

dict1 = defaultdict(int)
dict2 = defaultdict(set)
dict3 = defaultdict(str)
dict4 = defaultdict(list)
dict1[2] ='two'

print(dict1[1])
print(dict2[1])
print(dict3[1])
print(dict4[1])

输出：
0
set()

[]

'''
class Solution:
    def groupAnagrams1(self, strs: List[str]) -> List[List[str]]:
        """
        Time Complexity: O(NK \log K)O(NKlogK), where NN is the length of strs, and KK is the maximum length of a string in strs. The outer loop has complexity O(N)O(N) as we iterate through each string. Then, we sort each string in O(K \log K)O(KlogK) time.
        Space Complexity: O(NK)O(NK), the total information content stored in ans.
        :param strs:
        :return:
        """
        result = collections.defaultdict(list)
        for e in strs:
            result[tuple(sorted(e))].append(e)
        return result.values()

    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        '''
        Complexity Analysis
        Time Complexity: O(NK)O(NK), where NN is the length of strs, and KK is the maximum length of a string in strs. Counting each string is linear in the size of the string, and we count every string.
        Space Complexity: O(NK)O(NK), the total information content stored in ans.
        :param strs:
        :return:
        '''
        result = collections.defaultdict(list)
        for s in strs:
            count = [0] * 26
            for c in s:
                count[ord(c) - ord('a')] += 1
            result[tuple(count)].append(s)
        return result.values()
