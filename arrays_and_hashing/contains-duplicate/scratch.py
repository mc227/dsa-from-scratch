def containsDuplicate(nums):
    hashMap = {}

    for i in range(len(nums)):
        if nums[i] in hashMap:
            return True
        hashMap[nums[i]] = i
    return False
        

print(containsDuplicate([1,2,3,1]))