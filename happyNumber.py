'''
Write an algorithm to determine if a number is "happy".

A happy number is a number defined by the following process: Starting with any positive integer, replace the number by the sum of the squares of its digits, and repeat the process until the number equals 1 (where it will stay), or it loops endlessly in a cycle which does not include 1. Those numbers for which this process ends in 1 are happy numbers.

Example:

Input: 19
Output: true
Explanation:
12 + 92 = 82
82 + 22 = 68
62 + 82 = 100
12 + 02 + 02 = 1
'''


class Solution:

    def isHappy(self, n: int) -> bool:
        resultSet = set()
        result = 0
        while result != 1:
            result = 0

            while n > 0:
                result += (n%10) * (n%10)
                n //=10

            if result == 1:
                return True
            elif result in resultSet:
                return False
            else:
                n = result
                resultSet.add(result)

        def isHappy3(self, n: int) -> bool:
            resultSet = set()
            index = self.calculate(n)
            resultSet.add(index)
            result = self.calculate(index)

            while result not in resultSet:
                resultSet.add(result)
                result = self.calculate(result)
                print(result)
            if result == 1:
                return True
            else:
                return False

    def calculate(self, n: int) -> int:
        if n > 0:
            yu = n % 10
            return yu * yu + self.calculate(n // 10)
        else:
            return n


