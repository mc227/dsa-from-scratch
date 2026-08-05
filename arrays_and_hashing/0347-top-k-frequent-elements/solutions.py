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
        freq_list = {}
        for num in nums:
            if num in freq_list:
                freq_list[num] +=1
            else:
                freq_list[num] = 1
        # print(f"freq_list {freq_list}")
        foo = sorted(freq_list.values())[-k:]
        foo_list = []
        for k,v in freq_list.items():
            if v in foo:
                foo_list.append(k)
        return foo_list
    

# Do not edit any code below this line!

if __name__ == '__main__':
    import doctest
    count, _ = doctest.testmod()
    if count == 0:
        print('*** ALL TESTS PASS ***\nGive someone a HIGH FIVE!')