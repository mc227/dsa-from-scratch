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

>>> Solution().longestConsecutive([0,-1])
2
"""
from typing import List


class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if nums == []:
            return 0
        longestConsecutive = []
        consecutive = 1
        sorted_nums = sorted(nums)
        
        nodups_nums = list(tuple(dict.fromkeys(sorted_nums)))

        for i in range(len(nodups_nums)-1):
            if nodups_nums[i]+1 == nodups_nums[i+1]:
                consecutive+=1
            else:
                longestConsecutive.append(consecutive)
                consecutive = 1
        longestConsecutive.append(consecutive)
        return max(longestConsecutive)


# Do not edit any code below this line!

if __name__ == '__main__':
    import doctest
    count, _ = doctest.testmod()
    if count == 0:
        print('*** ALL TESTS PASS ***\nGive someone a HIGH FIVE!')