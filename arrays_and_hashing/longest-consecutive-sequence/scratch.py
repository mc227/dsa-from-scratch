from typing import List


class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        largest_num = max(nums)
        conceicao = 0
        bins = [0] * (largest_num+1)
        for num in nums:
            # print(num)
            bins[num] = 1
            # print(bins)
        for index, item in enumerate(bins):
            print(index, item)
        


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