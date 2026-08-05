from typing import List

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq_list = {}
        for num in nums:
            if num in freq_list:
                freq_list[num] +=1
            else:
                freq_list[num] = 1
        print(f"freq_list {freq_list}")
        foo = sorted(freq_list.values())[-k:]
        foo_list = []
        for k,v in freq_list.items():
            if v in foo:
                foo_list.append(k)
        return foo_list
    

# print(sorted(Solution().topKFrequent([1,1,1,2,2,3], 2)))
print(Solution().topKFrequent([1,1,1,2,2,3], 2))