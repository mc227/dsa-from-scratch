from typing import List

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashmap = {}
        for item in strs:
            freq_list = [0] * 26
            for letter in item:
                freq_list[ord(letter)-ord('a')]+=1
            freq_string = []
            char = 'a'
            for value in freq_list:
                freq_string.append(char)
                freq_string.append(str(value))
                char = chr(ord(char) + 1)
            freq_string = ''.join(freq_string)
            
            if freq_string not in hashmap:
                hashmap[freq_string] = [item]
            else:
                hashmap[freq_string].append(item)
                
        return list(hashmap.values())

                

print(Solution().groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"]))
# print(Solution().groupAnagrams(["eat","tea"]))
# [['eat', 'tea', 'ate'], ['tan', 'nat'], ['bat']]
# def groupAnagram(mylist):
#     main = {}
#     main_list = []
#     # loop through the list
#     # make a the hashmap counting the letters
#     # create the list of list. if a key's value is the same as another
#     for item in mylist:
#         hashmap = {}
#         for letter in item:
#             if letter in hashmap:
#                 hashmap[letter] += 1
#             else:
#                 hashmap[letter] = 1
#         # make the work the key in my dictionary
#         main[item] = hashmap


        
    
    # i have to append to the new list but i also need to delete 
    # TN said he practices under press
    # now 4:04
    # until 4:30
#     pass
        
        

# print(groupAnagram(["eat","tea","tan","ate","nat","bat"]))
# # [["bat"],["nat","tan"],["ate","eat","tea"]]