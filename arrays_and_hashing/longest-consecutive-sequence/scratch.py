from typing import List


class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        longestConsecutive = []
        consecutive = 1
        sorted_nums = sorted(nums)

        for i in range(len(sorted_nums)-1):
            if sorted_nums[i]+1 == sorted_nums[i+1]:
                consecutive+=1
            elif sorted_nums[i]+1 != sorted_nums[i+1]:
                longestConsecutive.append(consecutive)
                consecutive = 1
        print(longestConsecutive)
        # consider the last item also
        # return longestConsecutive
        


print(Solution().longestConsecutive([100, 4, 200, 1, 3, 2]))
# print(Solution().longestConsecutive([0,3,7,2,5,8,4,6,0,1]))
# print(Solution().longestConsecutive([1,0,1,2]))
# print(Solution().longestConsecutive([]))
# print(Solution().longestConsecutive([0,-1]))

'''
>>> Solution().longestConsecutive([100, 4, 200, 1, 3, 2])
4

>>> Solution().longestConsecutive([0, 3, 7, 2, 5, 8, 4, 6, 0, 1])
9

>>> Solution().longestConsecutive([1, 0, 1, 2])
3

>>> Solution().longestConsecutive([])
0

>>> Solution().longestConsecutive([0,-1])
2

'''