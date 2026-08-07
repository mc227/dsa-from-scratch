from typing import List


class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        # two pointers: i walks s, j walks t
        i = 0
        j = 0
        while i < len(s) and j < len(t):
            pass  # TODO
        return False


print(Solution().isSubsequence("abc", "ahbgdc"))


'''
>>> Solution().isSubsequence("abc", "ahbgdc")
True

>>> Solution().isSubsequence("axc", "ahbgdc")
False

>>> Solution().isSubsequence("", "ahbgdc")
True

>>> Solution().isSubsequence("abc", "")
False
'''