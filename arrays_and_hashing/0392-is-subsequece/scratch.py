from typing import List


class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        s_freq = {}
        t_freq = {}
        for item in s:
            if item in s_freq:
                s_freq[item] += 1
            else:
                s_freq[item] = 1
        for item in t:
            if item in t_freq:
                t_freq[item] += 1
            else:
                t_freq[item] = 1
        is_subset = s_freq.items() <= t_freq.items()
        return is_subset
        

# print(Solution().isSubsequence("abc", "ahbgdc"))
# print(Solution().isSubsequence("axc", "ahbgdc"))
# print(Solution().isSubsequence("", "ahbgdc"))
print(Solution().isSubsequence("abc", ""))

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