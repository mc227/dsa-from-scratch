'''

Let's solve the classic Two Sum problem. Given a list of integers and a
target, return the indices of the two numbers that add up to the target.

We call the method on an instance of Solution:

>>> Solution().twoSum([2, 7, 11, 15], 9)
[0, 1]

>>> Solution().twoSum([3, 2, 4], 6)
[1, 2]

>>> Solution().twoSum([3, 3], 6)
[0, 1]

>>> Solution().twoSum([2,5,5,11], 10)
[1, 2]

'''

from typing import List

# Write your code here:

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = {}

        for i in range(len(nums)):
            complement = target - nums[i]
            if complement in hashmap:
                return [hashmap[complement], i]
            hashmap[nums[i]] = i

# Do not edit any code below this line!

if __name__ == '__main__':
    import doctest
    count, _ = doctest.testmod()
    if count == 0:
        print('*** ALL TESTS PASS ***\nGive someone a HIGH FIVE!')