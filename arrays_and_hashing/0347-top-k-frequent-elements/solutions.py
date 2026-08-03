'''
>>> sorted(Solution().topKFrequent([1,1,1,2,2,3], 2))
[1, 2]

>>> sorted(Solution().topKFrequent([1], 1))
[1]

>>> sorted(Solution().topKFrequent([1,2,1,2,1,2,3,1,3,2], 2))
[1, 2]
'''

from typing import List

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        pass


# Do not edit any code below this line!

if __name__ == '__main__':
    import doctest
    count, _ = doctest.testmod()
    if count == 0:
        print('*** ALL TESTS PASS ***\nGive someone a HIGH FIVE!')