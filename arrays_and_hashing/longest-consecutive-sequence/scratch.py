from typing import List


class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if nums == []:
            return 0
        contains_negative_number = False
        negatives = []
        for i in nums:
            if i <= 0:
                contains_negative_number = True
                negatives.append(i)

        if contains_negative_number:
            return negatives            


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
            else:
                if foo:
                    mark.append(foo)
                    foo = 0
        if item:
            mark.append(foo)
        return max(mark)        
        


print(Solution().longestConsecutive([100, 4, 200, 1, 3, 2]))
print(Solution().longestConsecutive([0,3,7,2,5,8,4,6,0,1]))
print(Solution().longestConsecutive([1,0,1,2]))
print(Solution().longestConsecutive([]))
print(Solution().longestConsecutive([0,-1]))

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