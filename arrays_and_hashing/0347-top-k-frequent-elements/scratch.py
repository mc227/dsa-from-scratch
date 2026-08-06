from typing import List

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # get the frequency list first
        freq_list = {}
        list_of_lists = []
        result = []
        for item in nums:
            if item not in freq_list:
                freq_list[item] = 1
            else:
                freq_list[item] += 1
        
        list_of_lists = [[] for _ in range(0, len(nums)+1)]
        for key, value in freq_list.items():
            list_of_lists[value].append(key)
        print(f"freq_list {freq_list}")
        print(f"list_of_list {list_of_lists}")
        for value in reversed(list_of_lists):
            if value:
                for i in value:
                    if len(result) < k:
                        result.append(i)
        return result
        

# print(sorted(Solution().topKFrequent([1,1,1,2,2,3], 2)))
# print(Solution().topKFrequent([1,1,1,2,2,3], 2))
print(Solution().topKFrequent([1], 1))