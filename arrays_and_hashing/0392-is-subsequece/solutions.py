from typing import List


class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        """
        >>> Solution().isSubsequence("abc", "ahbgdc")
        True

        >>> Solution().isSubsequence("axc", "ahbgdc")
        False

        >>> Solution().isSubsequence("", "ahbgdc")
        True

        >>> Solution().isSubsequence("abc", "")
        False

        >>> Solution().isSubsequence("acb", "ahbgdc")
        False
        """
        # two pointers: i walks s, j walks t
        i = 0
        j = 0
        while i < len(s) and j < len(t):
            pass  # TODO
        return False


# Do not edit any code below this line!

if __name__ == '__main__':
    import doctest
    count, _ = doctest.testmod()
    if count == 0:
        print('*** ALL TESTS PASS ***\nGive someone a HIGH FIVE!')