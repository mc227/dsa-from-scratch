def isAnagram(s,t):
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

        
        

print(isAnagram("anagram","nagaram"))