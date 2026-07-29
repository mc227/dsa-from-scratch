'''
>>> Solution().groupAnagrams(["eat","tea","tan","ate","nat","bat"])
[['eat', 'tea', 'ate'], ['tan', 'nat'], ['bat']]

>>> Solution().groupAnagrams([""])
[['']]

>>> Solution().groupAnagrams(["a"])
[['a']]
'''

from typing import List

# Write your code here:

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        main = {}
        for item in strs:
            signature = tuple(sorted(item))
            main.setdefault(signature, []).append(item)
        return list(main.values())


# Do not edit any code below this line!

if __name__ == '__main__':
    import doctest
    count, _ = doctest.testmod()
    if count == 0:
        print('*** ALL TESTS PASS ***\nGive someone a HIGH FIVE!')