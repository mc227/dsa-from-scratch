from typing import List

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # get the frequency list first
        freq_list = {}
        list_of_lists = []
        for item in nums:
            if item not in freq_list:
                freq_list[item] = 1
            else:
                freq_list[item] += 1
        for i in range(len(nums)):
            list_of_lists.append([])
        for key, value in freq_list.items():
            list_of_lists[value].append(key)
        # given the length of nums create a list of list where we 
        # 0  1   2    3  4 5
        #   [3] [2]  [1] 
        #[[0],[3],[2],[1],[],[]]
        
        # the index of the list of list represents the number of occurence
        # and the list within that index contains the item being counted
        # lastly do len(list) < k loop from the top
        # don't sort just add the values until you output the topfrequent

        for i in range(len(list_of_lists)):
            print(i)

# print(sorted(Solution().topKFrequent([1,1,1,2,2,3], 2)))
print(Solution().topKFrequent([1,1,1,2,2,3], 2))