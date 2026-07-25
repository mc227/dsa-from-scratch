'''

>>> Solution().isAnagram("anagram","nagaram")
True

>>> Solution().isAnagram("rat","car")
False


'''

from typing import List

# Write your code here:

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        hashmap1 = {}
        hashmap2 = {}
        for letter in s:
            if letter in hashmap1:
                hashmap1[letter]+=1    
            else:
                hashmap1[letter] = 1
        for letter in t:
            if letter in hashmap2:
                hashmap2[letter]+=1    
            else:
                hashmap2[letter] = 1
        return hashmap1 == hashmap2
        


# Do not edit any code below this line!

if __name__ == '__main__':
    import doctest
    count, _ = doctest.testmod()
    if count == 0:
        print('*** ALL TESTS PASS ***\nGive someone a HIGH FIVE!')