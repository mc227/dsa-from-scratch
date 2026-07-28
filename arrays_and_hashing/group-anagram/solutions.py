'''

>>> Solution().groupAnagram(["eat","tea","tan","ate","nat","bat"])
[["bat"],["nat","tan"],["ate","eat","tea"]]

>>> Solution().groupAnagram([""])
[[""]]

>>> Solution().groupAnagram(["a"])
[["a"]]


'''

from typing import List

# Write your code here:

class Solution:
    def groupAnagram(self, strs: List[str]) -> List[List[str]]:        
        pass


# Do not edit any code below this line!

if __name__ == '__main__':
    import doctest
    count, _ = doctest.testmod()
    if count == 0:
        print('*** ALL TESTS PASS ***\nGive someone a HIGH FIVE!')