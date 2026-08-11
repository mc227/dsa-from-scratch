from typing import List


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
                # print(f"run starts at {n}, length {length}")
                if length > longest:
                    longest = length
        return longest


print(Solution().longestConsecutive([100, 4, 200, 1, 3, 2]))
# print(Solution().longestConsecutive([0,3,7,2,5,8,4,6,0,1]))
# print(Solution().longestConsecutive([1,0,1,2]))
# print(Solution().longestConsecutive([]))

'''
>>> Solution().longestConsecutive([100, 4, 200, 1, 3, 2])
4

>>> Solution().longestConsecutive([0, 3, 7, 2, 5, 8, 4, 6, 0, 1])
9

>>> Solution().longestConsecutive([1, 0, 1, 2])
3

>>> Solution().longestConsecutive([])
0
'''