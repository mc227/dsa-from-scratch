'''

>>> Solution().isAnagram("anagram","nagaram")
True

>>> Solution().isAnagram("rat","car")
False

>>> Solution().isAnagram("a","ab")
False

'''

from typing import List

# Write your code here:

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s = s.lower()
        t = t.lower()
    
        s = s.replace(" ","")
        t = t.replace(" ","")
    
        counts = [0] * 26
    
        for char in s:
            counts[ord(char) - ord('a')] += 1
    
        for char in t:
            counts[ord(char) - ord('a')] -= 1
        for count in counts:
            if count != 0:
                return False
        return True
        
        


# Do not edit any code below this line!

if __name__ == '__main__':
    import doctest
    count, _ = doctest.testmod()
    if count == 0:
        print('*** ALL TESTS PASS ***\nGive someone a HIGH FIVE!')