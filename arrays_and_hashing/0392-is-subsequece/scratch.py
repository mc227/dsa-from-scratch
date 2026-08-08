from typing import List


class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        # two pointers: i walks s, j walks t
        i = 0
        j = 0
        if len(s) == 0:
            return True
        if len(t) == 0:
            return False    
        while i < len(s) and j < len(t):
            if s[i] == t[j] and i<=j and i == (len(s)-1):
                return True
            elif s[i] == t[j] and i<=j:
                i+=1
                j+=1
                # print(f"inside if {i} {j}")
            else:
                j+=1
                # print(f"inside else {i} {j}")
        return False


# print(Solution().isSubsequence("abc", "ahbgdc"))
# print(Solution().isSubsequence("axc", "ahbgdc"))
print(Solution().isSubsequence("", "ahbgdc"))
# print(len(""))

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