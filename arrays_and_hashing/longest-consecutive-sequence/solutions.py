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
        largest_num = max(nums)
        foo = 0
        bins = [0] * (largest_num+1)
        for num in nums:
            # print(num)
            bins[num] = 1
        mark = []
        for item in bins:
            if item:
                foo+=1
            elif foo:
                    mark.append(foo)
                    foo = 0
        if item:
            mark.append(foo)
        return max(mark)        


# Do not edit any code below this line!

if __name__ == '__main__':
    import doctest
    count, _ = doctest.testmod()
    if count == 0:
        print('*** ALL TESTS PASS ***\nGive someone a HIGH FIVE!')