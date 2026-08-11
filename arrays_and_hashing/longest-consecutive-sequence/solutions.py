from typing import List

"""
>>> Solution().longestConsecutive([100, 4, 200, 1, 3, 2])
4

>>> Solution().longestConsecutive([0, 3, 7, 2, 5, 8, 4, 6, 0, 1])
9

>>> Solution().longestConsecutive([1, 0, 1, 2])
3

>>> Solution().longestConsecutive([])
0

>>> Solution().longestConsecutive([5])
1

>>> Solution().longestConsecutive([9, 1, 4, 7, 3, -1, 0, 5, 8, -1, 6])
7
"""


class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # dedupe so lookups are O(1) and each run is walked once
        num_set = set(nums)
        longest = 0
        for n in num_set:
            # only start counting at the head of a run
            if n - 1 not in num_set:
                length = 1
                while n + length in num_set:
                    length += 1
                if length > longest:
                    longest = length
        return longest


# Do not edit any code below this line!

if __name__ == '__main__':
    import doctest
    count, _ = doctest.testmod()
    if count == 0:
        print('*** ALL TESTS PASS ***\nGive someone a HIGH FIVE!')