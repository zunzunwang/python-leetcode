from typing import List


class Solution:
    """
    method1: use stack
    """

    def backspaceCompare(self, S: str, T: str) -> bool:
        return self.treatString(S) == self.treatString(T)

    def treatString(self, S: str) -> List[str]:
        result = []
        for c in S:
            if c is not '#':
                result.append(c)
            elif result and c == '#':
                result.pop()
        return result

    """
    method2: use O(n) time complexity and O(1) space complexity
    """

    def backspaceCompare2(self, S: str, T: str) -> bool:
        """
        Two index i and j
        """
        i = len(S) - 1
        j = len(T) - 1
        countS = countT = 0

        """
        while loop with or condition
        """
        while i >= 0 or j >= 0:
            """
            get last not # character
            cas 1: i point to a character
            cas 2: i point to -1
            """
            while i >= 0 and (S[i] == '#' or countS > 0):
                if S[i] == "#":
                    i -= 1
                    countS += 1
                elif countS > 0:
                    i -= 1
                    countS -= 1

            while j >= 0 and (T[j] == '#' or countT > 0):
                if T[j] == "#":
                    j -= 1
                    countT += 1
                elif countT > 0:
                    j -= 1
                    countT -= 1

            '''
            compare the result
            '''
            if i < 0 or j < 0:
                return i == j

            if S[i] != T[j]:
                return False
            else:
                i -= 1
                j -= 1
        return i == j
