def groupAnagrams(mylist):
    main = {}
    for item in mylist:
        hashmap = {}
        for letter in item:
            if letter in hashmap:
                hashmap[letter] = hashmap[letter]+1
            else:
                hashmap[letter] = 1
        signature = tuple(sorted(hashmap.items()))

        if signature in main:
            main[signature].append(item)
        else:
            main[signature] = [item]
    return list(main.values())


print(groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"]))
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