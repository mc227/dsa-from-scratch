'''

>>> Solution().containsDuplicate([1,2,3,1])
True

>>> Solution().containsDuplicate([1,2,3,4])
False

>>> Solution().containsDuplicate([1,1,1,3,3,4,3,2,4,2])
True


'''

from typing import List

# Write your code here:

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        hashMap = {}
        for i in range(len(nums)):
            if nums[i] in hashMap:
                return True
            hashMap[nums[i]] = i
        return False


# Do not edit any code below this line!

if __name__ == '__main__':
    import doctest
    count, _ = doctest.testmod()
    if count == 0:
        print('*** ALL TESTS PASS ***\nGive someone a HIGH FIVE!')